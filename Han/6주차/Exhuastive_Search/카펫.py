# 오답 76.9
def solution(brown, yellow):
    
    def Divisor(n):
        divisor = []
        for i in range(1, n + 1):
            if (n % i == 0) :
                divisor.append(i)
        return divisor
    
    number = Divisor(brown+yellow)
    pivot = int(len(number)/2)
    answer = []
    
    if len(number)%2 == 0:
        answer.append(number[pivot])
        answer.append(number[pivot-1]) 
    else:
        answer.append(number[pivot])
        answer.append(number[pivot])
        
    return answer