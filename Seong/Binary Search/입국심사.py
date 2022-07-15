def solution(n, times):
    answer = 0
    times.sort()
    min_time = min(times)
    max_time = max(times)*n
    while min_time <= max_time:
        mid = (min_time + max_time)//2
        passed = 0
        for t in times:
            passed += mid//t
            if passed >= n :
                break
        if passed < n:
            min_time = mid+1
            continue
        max_time = mid-1
        answer=mid
    return answer
