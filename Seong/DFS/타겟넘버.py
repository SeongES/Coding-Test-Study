import collections

def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        sum, trial = stack.popleft()

        if trial == len(numbers):
            if sum == target:
                answer += 1
        else:
            number = numbers[trial]
            stack.append((sum+number, trial + 1))
            stack.append((sum-number, trial + 1))

    return answer
  

print(solution([1, 1, 1, 1, 1],	3))
print(solution([4, 1, 2, 1], 4))
