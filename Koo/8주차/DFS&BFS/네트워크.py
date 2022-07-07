def solution(n, computers):
    answer = 0
    
    nt = [False for i in range(n)]
    
    for i in range(n) :
        if nt[i] == False : 
            dfs(n, computers, i, nt)
            answer += 1
    return answer

def dfs(n, computers, node, nt) :
    nt[node]  = True
    
    for i in range(n) :
        if i  != node and computers[node][i] == 1 :
            if nt[i] == False :
                dfs(n, computers, i, nt)
