##전화번호 목록
#hash
def solution(phone_book):
    answer = True
    dic = {}

    for pre in phone_book:
        dic[pre] = 0

    for pre in phone_book:
        tmp = ""
        for num in pre:
            tmp += num
            if tmp in dic and tmp!=pre:
                answer = False

    return answer