def solution(nums):
    answer = 0
    c1=len(nums)//2
    c2=len(set(nums))
    answer=min(c1,c2)
    return answer
