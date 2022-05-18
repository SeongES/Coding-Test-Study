# 완주하지 못한 선수
## hash value 이용
def solution(participant, completion):
    answer = ''
    dict = {}
    sum = 0
    
    for p in participant:
        dict[hash(p)] = p
        sum += hash(p)
    
    for c in completion:
        sum -= hash(c)
    
    answer = dict[sum]
    
    return dict[sum]