# 미완

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def factors(a,b):
    return factorial(a+b)/(factorial(a)*factorial(b))
    

def solution(m, n, puddles):
    answer = 0
    m,n= m-1, n-1
    
    a = (puddles[0][0])
    b = (puddles[0][1])
    a,b = a-1, b-1

    no_pad = factors(m,n)
    
    pad = factors(a,b) * factors(m-a, n-b)
    answer = no_pad - pad
    # 아직 puddle이 하나인 경우만
    # puddle 여러개인 경우 생각해야됨
    # for문으로 하나씩 뽑고 pad에 곱해가는
    return int(answer)
