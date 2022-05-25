def solution(array, commands):
    answer = []
    print('a')
    for command in commands:
        list_=array[(command[0]-1):(command[1])]
        list_.sort()
        answer.append(list_[command[2]-1])
        print(answer)
    return answer
