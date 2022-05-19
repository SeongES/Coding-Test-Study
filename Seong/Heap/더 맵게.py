# Level 2

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


'''
python - heapq 모듈 : binary tree 기반의 min heap 자료구조 제공
heapq.heappush(heap,7) - heap 에 7 추가
heapq.heappop(heap) - 가장 작은 원소 삭제
heapq.heapify(heap) - 리스트를 heap으로 변환

참고 사이트 : https://www.daleseo.com/python-heapq/
'''
