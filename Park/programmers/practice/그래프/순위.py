def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)] # Adjacency matrix
    for win, lose in results:
        matrix[win-1][lose-1] = True
        matrix[lose-1][win-1] = False
        
    # Floyd-Warshall algorithm
    ## 기본적인 논리는 j 점에서 k점을 갈 때 i 점을 거쳐 j -> i -> k로는 갈 수 있는가?
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[j][i] == None:
                    continue
                    
                if matrix[j][i] == matrix[i][k]:
                    matrix[j][k] = matrix[j][i]
                    matrix[k][j] = not matrix[j][i]
                    
    answer = 0
    for i in range(n):
        if None in matrix[i][:i] + matrix[i][i+1:]: # 스스로와 경기 결과를 제외하고 모두 들어 있으면 +1
            continue
        answer += 1
    return answer
