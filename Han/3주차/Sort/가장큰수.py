def solution(numbers):
    num = [str(num) for num in numbers]
    num = sorted(num, key = lambda x: x*3, reverse= True) # Default=ascend
    answer = str(int(''.join(num)))
    return answer

solution([6, 10, 2])