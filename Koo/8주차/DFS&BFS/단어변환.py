from collections import deque

def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited= [False for i in range(len(words))]

    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        
        for i, word in enumerate(words):
            if visited[i]:
                continue
            if len([i for i, w in enumerate(word) if now[i] != w ]) == 1:
                q.append((word, cnt + 1))
                visited[i] = True
    return 0
