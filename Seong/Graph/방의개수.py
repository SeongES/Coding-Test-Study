import collections

# 좌표가 아닌 중간지점에서 x교차 지점 고려가 중요

def solution(arrows):
    answer = 0
    # 0,1,2 arrow의 좌표 진행 방향 지정
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)

    # visited : 노드 방문
    # visited_dir : 노드 방문 경로
    visited = collections.defaultdict(int)
    visited_dir = collections.defaultdict(int)

    # arrows 따라 노드 좌표를 큐에 추가
    queue = collections.deque([now])
    for i in arrows:
        # 좌표와 좌표 사이의 X자로 교차하는 지점을 좌표로 표시하기 위해 2칸씩 이동
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            queue.append(next)
            now = next

    now = queue.popleft()
    visited[now] = 1

    while queue:
        next = queue.popleft()

        # 방문한 노드
        if visited[next] == 1:
            # 처음 온 경우에 방 +
            if visited_dir[(now, next)] == 0:
                answer += 1
        else:
            visited[next] = 1

        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next

    return answer
