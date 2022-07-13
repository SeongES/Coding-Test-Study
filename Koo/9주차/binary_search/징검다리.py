def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    l, r = 0, distance
    
    while l <= r :
        mid = (l + r) // 2 # 바위 사이 최소 거리
        rm_cnt = 0  # 제거한 바위 개수
        prev = 0    # 이전 바위(거리계산용)
        
        for rock in rocks :
            if rock - prev < mid :
                rm_cnt += 1
            else :
                prev = rock
        
        if rm_cnt > n :
            r = mid - 1
        else : 
            answer = mid
            l = mid + 1
                
    return answer
