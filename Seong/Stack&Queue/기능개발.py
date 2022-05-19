def solution(progresses, speeds):
    answer = []
    
    days = []
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds [i] ==0 :
            days.append((100 - progresses[i]) // speeds [i])
        else:
            days.append(((100 - progresses[i]) // speeds [i]) +1)
    
    cnt = 0
    max_day = days[0]
    
    for l in range(len(days)):
        if max_day < days[l]:
            max_day = days[l]
            answer.append(cnt)
            cnt = 1
           
        else :
            cnt += 1
    answer.append(cnt)
    
    return answer
