def solution(people, limit):
    answer = len(people)
    people.sort()
    i, j = len(people) - 1, 0
    
    while i > j :
        if people[i] + people[j] <= limit :
            j += 1
            answer -= 1
        i -= 1
    
    return answer
