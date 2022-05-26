# 오답

# 해당 숫자가 소수인지 아닌지 확인
def check_prime(num):
    if num == 1 or num ==0 :
        return False
    for i in range(2, int(num/2)+1):
        if num%i == 0 :
            result = False
    return True

# 가능한 수 조합수
def search_numbers(numbers, i, check_num, prime_list):
    for j in numbers:
        num = i + j
        rem = numbers.replace(j, '', 1)
        if int(num) not in check_num:
            check_num.append(int(num))
            if check_prime(int(num)):
                prime_list.append(int(num))
        if rem:
            search_numbers(rem, num, check_num, prime_list)

def solution(numbers):
    check_num = []
    prime_list = []
    answer = 0
    for i in numbers:
        # 확인한 수는 check num에
        if int(i) not in check_num:
            check_num.append(int(i))
            # 소수이면 prime list에
            if check_prime(int(i)):
                prime_list.append(int(i))
        # 뽑은 수 외에 다른 숫자와의 조합 찾기
        rem = numbers.replace(i,'',1)
        search_numbers(rem, i, check_num, prime_list)
    answer = len(prime_list)
    return answer
