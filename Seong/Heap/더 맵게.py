import heapq
        
def solution(scoville, K):
    answer = 0
    # 기존 리스트를 힙으로 변환
    scov = heapq.heapify(scoville)
    
    while scoville[0] < K :
        if len(scoville) == 1:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        mep = a+b*2
        heapq.heappush(scoville,mep)
        answer += 1



    return answer
