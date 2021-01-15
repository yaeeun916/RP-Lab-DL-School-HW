def check_parentheses(input_expression): #input의 형태는 string
    input_expression=list(input_expression)
    checked='Balanced'
    for (i, j) in [('(', ')'), ('{', '}'), ('[', ']')]: 
        if input_expression.count(i)!=input_expression.count(j): #괄호가 쌍으로 존재하지 않으면 불완결
            checked='Unbalanced'
            break #하나라도 불완결이면 더 확인할 필요 없음
        else:
            while i in input_expression:
                if input_expression.index(i)>input_expression.index(j): #괄호의 순서가 거꾸로면 불완결
                    checked='Unbalanced'
                    break #하나라도 불완결이면 더 확인할 필요 없음. while문 break
                break #for문 break
                input_expression.remove(i) #.index(item)은 첫번째로 나온 item의 index. 여러개일 경우 지워가며 확인해
                input_expression.remove(j)
    return checked
                
        
#괄호의 순서가 문제되는건 ()을 예로 들었을 때 가장 먼저 나오는 ()괄호가 )이거나 가장 마지막이 (
#문제점: else 문에서[(  )  (  ) ]에 대해선
#                    ^  ^이 둘을 확인하는데
#                   [((  ))]에 대해선
#                    ^   ^ 이 둘을 확인
