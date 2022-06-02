def solution(citations):
    answer = 0
    citations.sort()
    
    for i, item in enumerate(citations) :
        if len(citations) - i >= item :
            answer = item
        else :
            answer = max(min(len(citations) - i, item), answer)
    return answer
