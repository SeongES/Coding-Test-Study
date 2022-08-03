def solution(arr):
    answer = []
    
    for i in arr : 
        if answer :
            if i != answer[-1] :
                answer.append(i)
        else :
            answer.append(i)
    
    return answer
  
  # 위의 if 조건문들을 하나로 줄일 수 있음 (슬라이스해서 배열 대 배열으로 비교하면 빈 배열일 때 error 뜨지않음)
  
  def solution(arr):
    answer = []
    
    for i in arr : 
        
        if answer[-1:] == [i] : continue
        answer.append(i)
        '''
        if answer :
            if i != answer[-1] :
                answer.append(i)
        else :
            answer.append(i)
        '''
    return answer
