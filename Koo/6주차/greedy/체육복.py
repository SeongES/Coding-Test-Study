def solution(n, lost, reserve):
    answer = 0
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)
    #reserve = [i for i in reserve if i-1 not in lost]
    #lost = [i for i in lost if i+1 not in reserve]
    for i in reserve :
        if i - 1 in lost : 
            lost.remove(i-1)
        elif i + 1 in lost :
            lost.remove(i+1)
        
    answer = n - len(lost)
    return answer
