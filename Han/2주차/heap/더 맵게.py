def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        try: 
            term1 = heapq.heappop(scoville)
            term2 = heapq.heappop(scoville)
            
            heapq.heappush(scoville, term1 + term2 * 2)
            answer += 1
        except IndexError:
            return -1  
    
    return print(answer)

solution([1, 2, 3, 9, 10, 12], 7)