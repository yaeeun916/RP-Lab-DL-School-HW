#example 1

def pair_count(input_list):  #예: input_list=['bcd', 'bce', 'cce']
    pair_count=0
    for i in range(len(input_list)):
        input_list[i]=set(list(input_list[i])) #예: input_list=[{'b', 'c', d'}, {'b', 'c', 'e'}, {'c', 'e'}]
    for i in input_list:
        for j in input_list:
            if i!=j and len(list(i&j))==2: #서로 다른 두 set의 교집합의 원소가 2일 때
                pair_count+=1
            else:
                pass
    pair_count=int(pair_count/2) 
    return(pair_count) #소수점이 나오지 않도록
    
