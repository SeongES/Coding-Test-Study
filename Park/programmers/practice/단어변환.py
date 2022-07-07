# BFS
from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [ 0 for i in range(len(words))]
    while q:
        word, cnt = q.popleft() # word : begin부터 시작하여 target으로 변환중인 word, cnt : count
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0 # word와 각 words안의 문자와 비교하여 서로 다른 알파벳 총 개수.
            if not V[i]: # 초기 V는 0(False)이 저장돼 있음.
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1]) # BFS > e.g. ([word1, 1],[word5,1],[word7,1])
                    V[i] = 1
                    
    return answer
