# 오답 90.0
def solution(n, lost, reserve):
    
    new_reserve = [i for i in reserve if i not in lost]
    new_lost = [i for i in lost if i not in reserve]
    
    for i in new_reserve:
        if (i-1) in new_lost:
            new_lost.remove(i-1)
        elif (i+1) in new_lost:
            new_lost.remove(i+1)
            
    
    answer = n-len(new_lost)
    return answer