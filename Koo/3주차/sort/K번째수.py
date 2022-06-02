def solution(array, commands):
    answer = []
    
    for arr in commands :
        temp = []
        for i, item in enumerate(array):
            if i >= arr[0]-1 and i <= arr[1]-1 :
                temp.append(item)
        temp.sort()
        answer.append(temp[arr[2]-1])
        
    return answer
