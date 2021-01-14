def sort_tuple(dict1):
    dict2={} #입력한 dict1와 key, value가 서로 바뀐 dictionary
    sorted=() #반환할 tuple
    for i, j in dict1.items():
        dict2[j]=i #key, value 바꾸기
    dict2keys=list(dict2.keys())
    dict2keys.sort() #dict2의 key(=dict1의 value)를 기준으로 오름차순 정렬
    for i in dict2keys:
        sorted=sorted+(dict2[i],) 
    return sorted
            
