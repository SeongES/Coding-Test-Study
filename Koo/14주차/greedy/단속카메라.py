def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x : x[1])
    current = -99999
    
    for route in routes : 
        if current < route[0] :
            current = route[1]
            answer += 1
    return answer
