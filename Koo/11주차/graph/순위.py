def solution(n, results):
    graph = [[0]*(n+1) for _ in range(n+1)]
    
    for result in results:
        graph[result[0]][result[1]] = 1
        graph[result[1]][result[0]] = -1
        
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                for k in range(1, n+1):
                    if graph[j][k] == 1 and graph[i][k] == 0:
                        graph[i][k] = 1
                        graph[k][i] = -1
            elif graph[i][j] == -1:
                for k in range(1, n+1):
                    if graph[j][k] == -1 and graph[i][k] == 0:
                        graph[i][k] = -1
                        graph[k][i] = 1
            
    count = 0        
    for i in range(1, n+1):
        if graph[i][1:].count(0) == 1:
            count += 1
    
    return count

#비트연산 사용

from collections import defaultdict


def solution(n, results):
    wins = defaultdict(set)
    loses = defaultdict(set)
    
    for winner, loser in results:
        wins[winner].add(loser)
        loses[loser].add(winner)
    
    for i in range(1, n+1):
        for loser in wins[i]:
            loses[loser] |= loses[i]
        for winner in loses[i]:
            wins[winner] |= wins[i]
    
    count = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            count += 1
    
    return count

#Floyd-Warshell 알고리즘 사용

def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)]
    for win, lose in results:
        matrix[win-1][lose-1] = True
        matrix[lose-1][win-1] = False
        
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
        if None in matrix[i][:i] + matrix[i][i+1:]:
            continue
        answer += 1
    return answer
