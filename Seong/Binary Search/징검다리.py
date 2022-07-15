def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    min_d , max_d = 0, distance
    while min_d <= max_d :
        mid = (min_d + max_d)
        current, removed = 0, 0
        mins = float('inf')
        for rock in rocks:
            if rock-current < mid:
                removed+=1
            else:
                dist = min(mins, rock - current)
                current = rock
        if removed > n:
            max_d = mid - 1
        else:
            min_d = mid + 1
            answer = mins
    return answer
