# 초기버전
import heapq
def solution(operations):
    queue = []
    answer = []
    
    for op in operations :
        if 'I' in op :
            num = int(op.split()[-1])
            heapq.heappush(queue, num)
        elif op == 'D 1' and queue :
            queue = queue[:-1]
            queue.sort()
        elif op == 'D -1' and queue :
            heapq.heappop(queue)
    
    if queue :
        answer =  [heapq.nlargest(1, queue)[0], heapq.nsmallest(1, queue)[0]]
    else :
        answer = [0, 0]

    return answer
  
# 좀 더 갈무리한 버전
import heapq
def solution(operations):
    queue = []
    answer = []
    
    for op in operations :
        if 'I' in op :
            num = int(op.split()[-1])
            heapq.heappush(queue, num)
        else :
            if queue :
                if op == 'D 1' : queue.pop(queue.index(heapq.nlargest(1, queue)[0]))
                else : heapq.heappop(queue)
    
    if queue :
        answer =  [heapq.nlargest(1, queue)[0], heapq.nsmallest(1, queue)[0]]
    else :
        answer = [0, 0]

    return answer
