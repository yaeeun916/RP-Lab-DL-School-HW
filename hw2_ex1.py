# -*- coding: utf-8 -*-
!pip install idx2numpy
!pip install scikit-image

#IMPORTS
import os
import urllib.request
import gzip
import idx2numpy
import numpy as np
from skimage.io import imsave

def MNISTdownload(path): #다운로드 경로는 함수의 인자로 입력 
  #다운로드 경로 생성 
  if not os.path.exists(path):
      os.makedirs(path)
 
  # http://yann.lecun.com/exdb/mnist/ 에서 MNIST dataset 다운로드
  hrefs=["train-labels-idx1-ubyte.gz","train-images-idx3-ubyte.gz", "t10k-labels-idx1-ubyte.gz", "t10k-images-idx3-ubyte.gz"]
  for href in hrefs: 
    if not os.path.exists(os.path.join(path,href)): #동일 경로에 다운받은적 없다면
      url = "http://yann.lecun.com/exdb/mnist/"+href 
      urllib.request.urlretrieve(url, os.path.join(path,href)) #urlretrieve함수를 통해 원하는 경로에 .gz 파일 다운로드
 
  #이미지 저장 디렉토리 생성
  if not os.path.exists(os.path.join(path,'mnist_dataset')):
    os.makedirs(os.path.join(path,'mnist_dataset'))
    os.makedirs(os.path.join(path,'mnist_dataset/train'))
    os.makedirs(os.path.join(path,'mnist_dataset/test'))
    for i in range(10):
      os.makedirs(os.path.join(path,'mnist_dataset/train/%d'%i))
      os.makedirs(os.path.join(path,'mnist_dataset/test/%d'%i))
 
  #training set(60000 examples)
  with gzip.open(os.path.join(path,hrefs[0]), 'rb') as f_train_label: #training set의 label 압축 해제
    arr_train_label=idx2numpy.convert_from_file(f_train_label) #np.ndarray 반환
  with gzip.open(os.path.join(path,hrefs[1]), 'rb') as f_train_image: #training set의 image 압축 해제
    arr_train_image=idx2numpy.convert_from_file(f_train_image) #np.ndarray 반환
  for i in range(60000): #training set 내 모든 example에 대해 
    filenumber=len(os.listdir(os.path.join(path,'mnist_dataset/train/%d'%arr_train_label[i]))) #파일 이름 붙이기: label에 해당하는 폴더 내 파일 수
    imsave(os.path.join(path,'mnist_dataset/train/%d/%d.png'%(arr_train_label[i],filenumber)), arr_train_image[i]) #arr_train_image[i]를 이미지로 parsing해서 적절한 경로에 저장
        
  #test set(10000 examples)
  with gzip.open(os.path.join(path,hrefs[2]), 'rb') as f_test_label: #test set의 label 압축 해제
    arr_test_label=idx2numpy.convert_from_file(f_test_label) #np.ndarray 반환
  with gzip.open(os.path.join(path,hrefs[3]), 'rb') as f_test_image: #test set의 image 압축 해제
    arr_test_image=idx2numpy.convert_from_file(f_test_image) #np.ndarray 반환
  for i in range(10000): #test set 내 모든 example에 대해 
    filenumber=len(os.listdir(os.path.join(path,'mnist_dataset/test/%d'%arr_test_label[i]))) #파일 이름 붙이기: label에 해당하는 폴더 내 파일 수
    imsave(os.path.join(path,'mnist_dataset/test/%d/%d.png'%(arr_test_label[i],filenumber)), arr_test_image[i]) #arr_test_image[i]를 이미지로 parsing해서 적절한 경로에 저장
