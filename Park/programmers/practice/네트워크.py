# DFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)] # 트리 scan 기록.
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True # 연결된 컴퓨터는 True로 6번째 if문에 빠지지 않음.
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False: # 2 > 1로 거꾸로 못 감.
                DFS(n, computers, connect, visited) # 자식 노드로 내려 감.
