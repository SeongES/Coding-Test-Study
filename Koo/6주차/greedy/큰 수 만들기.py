def solution(number, k):
    answer = ''
    num_st = []
    
    for num in number :
        while num_st and num_st[-1] < num and k > 0 :
            num_st.pop()
            k -= 1
        num_st.append(num)
    
    if k != 0 :
        num_st = num_st[:-k]
        
    answer = answer.join(num_st)
    
    return answer
