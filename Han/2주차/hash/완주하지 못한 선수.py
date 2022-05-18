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

if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
