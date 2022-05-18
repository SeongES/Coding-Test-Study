## Runtime Error

from collections import deque

def solution(priorities, location):

    deq = deque(priorities)
    idx = deque([i for i in range(len(priorities))])
    tar = priorities[location]
    
    for num in priorities:
        if num < max(deq):
            deq.rotate(-1)
            idx.rotate(-1)
        else:
            break
    answer = list(idx).index(tar)             

    return print(answer)

#solution([2, 1, 3, 2], 2)
#solution([1, 1, 9, 1, 1, 1], 0)