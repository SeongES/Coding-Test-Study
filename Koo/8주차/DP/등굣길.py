def solution(m, n, puddles):
    answer = 0
    roads = [[0 for i in range(m+1)] for j in range(n+1)]
    roads[1][1] = 1
    
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if [j,i] in puddles :
                continue
            if i == 1 and j == 1 :
                continue
            roads[i][j] = roads[i-1][j] + roads[i][j-1]
    answer = roads[-1][-1] % 1000000007
        
    return answer
