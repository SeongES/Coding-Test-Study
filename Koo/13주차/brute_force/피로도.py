import itertools

def solution(k, dungeons):
    answer = -1
    
    for pm in itertools.permutations(dungeons, len(dungeons)) :
        fatigue = k 
        d_cnt = 0
        
        for l, s in pm :
            if fatigue >= l :
                fatigue -= s
                d_cnt += 1
        answer = max(answer, d_cnt)
    return answer
