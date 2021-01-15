#길이가 2일 때
def subsequences2(iterable):
    itList=list(iterable)
    sub=()
    for i in range(len(itList)):
        for j in range(i+1, len(itList)):
            sub=sub+(str(itList[i])+str(itList[j]),)
    return sub
            
#길이가 3일 때
def subsequences3(iterable):
    itList=list(iterable)
    sub=()
    for i in range(len(itList)):
        for j in range(i+1, len(itList)):
            for k in range(j+1, len(itList)):
                sub=sub+(str(itList[i])+str(itList[j])+str(itList[k]),)
    return sub


#길이가 n일 때로 확장하면?
#원소의 개수가 n인 부분집합 모두 출력
