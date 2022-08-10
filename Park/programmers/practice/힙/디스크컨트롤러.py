import heapq

# 1. jobs 배열은 소요시간을 기준으로 오름차순 정렬을 한다. 소요시간이 작을수록 각 작업들이 기다리는 시간이 줄어들기 때문이다.
# 2. jobs 배열이 empty가 될때까지 while문을 돌린다.
# 3. jobs 길이만큼 for문을 돌리면서 해당 작업의 요청시간이 start(현재까지 진행된 작업 시간)보다 작으면,
#    즉, 해당 작업이 진행된 시간보다 먼저 요청이 들어왔으면 해당 작업을 진행시키고 jobs 배열에서 지워버린다.

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)
