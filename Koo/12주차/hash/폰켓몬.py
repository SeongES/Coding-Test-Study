def solution(nums):
    answer = 0
    
    nums.sort()
    cnt = 0
    c_type = 0
    
    for i in nums :
        if c_type != i :
            cnt += 1
        c_type = i
  
    return len(nums) / 2 if len(nums) / 2 < cnt else  cnt
  
  # 더 간단한 버전
  def solution(nums):
    
    return min(len(nums)/2, len(set(nums)))
