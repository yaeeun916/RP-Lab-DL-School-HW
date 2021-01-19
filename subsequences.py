def subseq(iterable, n):
    itlist=[str(i) for i in iterable] #str으로 바꿔야 + 연산시 문제가 없다
    if n==1:
        return itlist 
    elif n==len(iterable):
        itlist2=[''.join(itlist)]
        return itlist2
        
    alist=[] #점화식 nCr=(n-1)C(r-1)+(n-1)Cr 사용한 재귀함수
    for i in subseq(itlist[1:], n-1): #(n-1)C(r-1)
      alist.append(itlist[0]+i)
    for i in subseq(itlist[1:], n): #(n-1)Cr
      alist.append(i)

    return alist

    


#종료조건을 하나로 줄일 수 있다
def subseq(iterable, n):
    itlist=[str(i) for i in iterable] #str으로 바꿔야 + 연산시 문제가 없다
    if n==1:
        return itlist 
        
    alist=[] #점화식 nCr=(n-1)C(r-1)+(n-2)C(r-1)+....+(r-1)C(r-1)
    for i in range(len(iterable)-(n-1)):
      for k in subseq(itlist[i+1:], n-1):
        alist.append(itlist[i]+k)

    return alist
