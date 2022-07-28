# 다익스트라 알고리즘 사용
import heapq

def solution(n, edge):
    answer = 0
    distance = [int(1e9)] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for i in edge :
        graph[i[0]].append((i[1], 1))
        graph[i[1]].append((i[0], 1))
        
    dijkstra(1, distance, graph)
    distance.pop(0)
    
    for i in distance :
        if i == max(distance) :
            answer += 1
        
    
    return answer

def dijkstra(start, distance, graph) :
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q :
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist :
            continue
        
        for i in graph[now] : 
            cost = dist + i[1]
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# BFS 방식

def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    distance = [float('-inf')] * (n+1)
    
    queue = [1]
    visited[1] = True
    distance[1] = 0
    
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    while queue:
        now = queue.pop(0)
        
        for node in graph[now]:
            if visited[node] == False:
                distance[node] = distance[now] + 1
                visited[node] = True
                queue.append(node)
        
    distance.sort(reverse = True)
    answer = distance.count(distance[0])
    
    return answer
