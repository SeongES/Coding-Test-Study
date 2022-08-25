def solution(money):
    n = len(money)
    dp_f = [0] * n
    dp_nf = [0] * n
    dp_f[0] = dp_f[1] = money[0]
    
    dp_nf[1] = money[1]
    dp_nf[2] = max(money[1], money[2])
    
    for i in range(2, n - 1) :
        dp_f[i] = max(dp_f[i - 1], dp_f[i - 2] + money[i])
    
    for i in range(2, n) :
        dp_nf[i] = max(dp_nf[i - 1], dp_nf[i - 2] + money[i])
        
    return max(dp_f[n - 2], dp_nf[n - 1])
