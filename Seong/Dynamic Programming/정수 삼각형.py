
def solution(triangle):
    answer = 0
    answer += triangle[0][0]
    # 첫번째 꺼 뺴고 두번째꺼부터 비교
    
    dp = [0] * len(triangle)
    dp[0] = triangle[0]
    for i in range(1,len(triangle)): 
        dp[i] = [0] * (i+1)
        for j in range(i+1):
            if j==0:
                dp[i][j] = dp[i-1][j] + triangle[i][j] #맨 왼쪽
            elif j==i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j] #끝쪽일떄
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j] # 가운데에서는 비교
            
    answer = max(dp[len(triangle)-1])
    return answer

