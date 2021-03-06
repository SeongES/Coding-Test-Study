def calculate_n(X, Y):
    n_set = set()
    for x in X:
        for y in Y:
            n_set.add(x+y)
            n_set.add(x-y)
            n_set.add(x*y)
            if y != 0:
                n_set.add(x//y)
    return n_set

def solution(N, number):
    answer = -1
    result = {}   
    result[1] = {N} 
    if number == N:
        return 1
    for n in range(2, 9):  
        i = 1
        temp_set = {int(str(N)*n)}  # 5, 55, 555, 5555
        
        while i < n:
            temp_set.update(calculate_n(result[i], result[n-i]))
            i += 1
        print(temp_set)

        if number in temp_set:
            answer = n
            break

        result[n] = temp_set

    return answer
