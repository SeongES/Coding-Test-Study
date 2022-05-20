def solution(progresses, speeds):   # list 말고 다른 구조로 구현해보기.
                                    # queue 클래스나 collections deque를 사용하면 수정하기 귀찮?
    queue = []
    answer = []
    for i in range(len(progresses)) : 
        queue.append([progresses[i], speeds[i]])
    
    while len(queue) : 
        done_p = 0
        for item in queue :
            item[0] += item[1]
        
        while len(queue) :
            if (queue[0][0] >= 100) :
                queue.pop(0)
                done_p += 1
            else :
                break
        if (done_p != 0) : answer.append(done_p)
    
    
    return answer
