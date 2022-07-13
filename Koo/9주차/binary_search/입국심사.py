def solution(n, times):
    answer = 0
    l, r = 0, max(times) * n    # 심사 시 걸리는 시간의 최소, 최대 값 설정
    
    
    while l <= r : 
        checked_p = 0   # 입국 심사 완료한 사람들 수
        mid = (l + r) // 2  # 모든 사람 심사 시 걸리는 시간
        
        for i in times :
            checked_p += mid // i
         
        if checked_p >= n : # 심사 완료한 사람의 수가 심사 해야하는 수보다 많거나 같을 시
            answer = mid    # right의 범위를 줄인다
            r = mid - 1
        elif checked_p < n :    # 심사 완료한 사람의 수가 심사 해야하는 사람의 수보다 적다면 left 범위 증가
            l = mid + 1
        
    return answer
