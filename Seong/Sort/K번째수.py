def solution(array, commands):
    answer = []
    for c in commands:
        k = array[c[0]-1:c[1]]
        k.sort()
        ans = k[c[2]-1]
        answer.append(ans)
    return answer
