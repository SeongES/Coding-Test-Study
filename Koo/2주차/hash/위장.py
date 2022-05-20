def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for n, c in clothes :
        clothes_dict[c] = clothes_dict.get(c, 0) + 1
    
    for i in clothes_dict.values() : 
        answer *= i+1
        
    return answer - 1
