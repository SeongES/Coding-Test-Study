import collections
def solution(n, vertex):
    dists = {i:0 for i in range(1, n+1)}  # 노드 1과 i간의 거리를 저장하는 딕셔너리 객체
    edge = collections.defaultdict(list)
    
    for v, u in vertex:                   # 양방향이기 때문에 u와 v에 각각 v, u를 추가합니다.
        edge[v].append(u)
        edge[u].append(v)

    # 1번 노드부터 BFS 알고리즘을 통해 순회합니다.
    # Queue에서 pop한 노드의 dists가 0이면(아직 방문하지 않았다면) 거리를 입력하고 해당 노드의 연결 노드를 Queue에 추가합니다.
    # Queue가 Empty 상태일 때까지 while문으로 순회합니다.
    q = collections.deque(edge[1])        
    dist = 1 
    while q:                              
        for i in range(len(q)):
            v = q.popleft()
            
            if dists[v] == 0: # 초기값인 0일 때만 dist를 저장하기 때문에 1 > 2 > 3으로 가는 경우는 dists에 값이 저장되지 않음.
                dists[v] = dist
                
                for w in edge[v]:
                    q.append(w) # list 형태의 다음 연결 노드 정보를 추가.
        dist += 1        
    
    del dists[1]                          # 1번 노드로부터 가장 멀리 떨어진 노드를 찾는 것이기 때문에, 1번 노드에 대한 거리 정보는 삭제합니다.
    
    max_value = max(dists.values())
    
    answer = 0
    for v in dists.values():              # 최대 거리를 구하고, dists에서 최대거리와 같은 노드의 갯수를 체크하여 반환합니다.
        if v == max_value:
            answer += 1
        
    return answer
