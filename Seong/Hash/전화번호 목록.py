def solution(phone_book):
    answer = True
    
    phone_hash = {}
    for phone in phone_book:
        phone_hash[phone]=1
    
    for phone in phone_book:
        temp=""
        for num in phone:
            temp += num
            if temp in phone_hash and temp!= phone:
                answer = False
    return answer
