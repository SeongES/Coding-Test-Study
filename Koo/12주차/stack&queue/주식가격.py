# 블로그에서 보고 좋은 풀이라 가져와봤음
def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = [0]
  
    for i in range(1, len(prices)) :
        while stack and prices[stack[-1]] > prices[i] :
            j = stack.pop()
            answer[j] = i - j
        
        stack.append(i)
    return answer
