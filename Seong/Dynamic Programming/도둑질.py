def solution(money):
    # 집이 이어져있어서 1번 집을 털면 마지막을 안 털고, 마지막을 털면 1번을 안 털도록

    # 1번 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, len(money)-1): 
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    # 마지막번 터는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): 
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대
