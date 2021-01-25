# -*- coding: utf-8 -*-
def MNISTdownload(path): #다운로드 경로는 함수의 인자로 입력 (입력값은 /로 끝나야 함)
  #IMPORTS
  import os
  import urllib.request
  import gzip
  !pip install idx2numpy
  import idx2numpy
  import numpy as np
  !pip install scikit-image
  from skimage.io import imsave

  #다운로드 경로 생성
  datapath = path 
  if not os.path.exists(datapath):
      os.makedirs(datapath)

  # http://yann.lecun.com/exdb/mnist/ 에서 MNIST dataset 다운로드
  hrefs=["train-labels-idx1-ubyte.gz","train-images-idx3-ubyte.gz", "t10k-labels-idx1-ubyte.gz", "t10k-images-idx3-ubyte.gz"]
  for href in hrefs: 
    url = "http://yann.lecun.com/exdb/mnist/"+href 
    urllib.request.urlretrieve(url, datapath+href) #urlretrieve함수를 통해 원하는 경로에 .gz 파일 다운로드

  #이미지 저장 디렉토리 생성
  os.makedirs(datapath+'mnist_dataset')
  os.makedirs(datapath+'mnist_dataset/train')
  for i in range(10):
    os.makedirs(datapath+'mnist_dataset/train/%d'%i)
  os.makedirs(datapath+'mnist_dataset/test')
  for i in range(10):
    os.makedirs(datapath+'mnist_dataset/test/%d'%i)

  #training set(60000 examples)
  with gzip.open(datapath+hrefs[0], 'rb') as f_train_label: #training set의 label 압축 해제
    arr_train_label=idx2numpy.convert_from_file(f_train_label) #np.ndarray 반환
  with gzip.open(datapath+hrefs[1], 'rb') as f_train_image: #training set의 image 압축 해제
    arr_train_image=idx2numpy.convert_from_file(f_train_image) #np.ndarray 반환
  for i in range(60000): #training set 내 모든 example에 대해 
    for j in range(10):
      if arr_train_label[i]==j:#label이 0~9중 무엇인지
        filenumber=len(os.listdir(datapath+'mnist_dataset/train/%d'%j)) #파일 이름 붙이기: label에 해당하는 폴더 내 파일 수
        imsave(datapath+'mnist_dataset/train/%d/%d.png'%(j,filenumber), arr_train_image[i]) #arr_train_image[i]를 이미지로 parsing해서 적절한 경로에 저장
        
  #test set(10000 examples)
  with gzip.open(datapath+hrefs[2], 'rb') as f_test_label: #test set의 label 압축 해제
    arr_test_label=idx2numpy.convert_from_file(f_test_label) #np.ndarray 반환
  with gzip.open(datapath+hrefs[3], 'rb') as f_test_image: #test set의 image 압축 해제
    arr_test_image=idx2numpy.convert_from_file(f_test_image) #np.ndarray 반환
  for i in range(10000): #test set 내 모든 example에 대해 
    for j in range(10):
      if arr_test_label[i]==j:#label이 0~9중 무엇인지
        filenumber=len(os.listdir(datapath+'mnist_dataset/test/%d'%j)) #파일 이름 붙이기: label에 해당하는 폴더 내 파일 수
        imsave(datapath+'mnist_dataset/test/%d/%d.png'%(j,filenumber), arr_test_image[i]) #arr_test_image[i]를 이미지로 parsing해서 적절한 경로에 저장
