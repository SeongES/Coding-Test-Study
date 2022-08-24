def solution(n, costs):
    costs.sort(key = lambda x:x[2]) # cost 기준 오름차순

    # cost 가장 작은 첫번째거 방문
    ans = costs[0][2]

    visited = set([costs[0][0], costs[0][1]])
    costs.pop(0)

    i = 0    
    while(len(visited) < n):
        if costs[i][0] in visited or costs[i][1] in visited: # 일차 방문한 지점에서 이어서 방문
            if costs[i][0] in visited and costs[i][1] in visited:	#사이클 방지
                i += 1
                continue
            ans += costs[i][2]
            visited = visited.union(costs[i][:2])
            del costs[i]
            i = 0
            continue
        i += 1

    return ans
