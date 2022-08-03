def solution(s):
    answer = True
    st = []
    
    for p in s :
        if p == '(' :
            st.append(p)
        elif p == ')' :
            try :
                st.pop()
            except IndexError :
                return False
    

    return len(st) == 0
    
    
# 다른 사람 풀이 if-elif 부분을 더 함축하여 표현
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
        
    return x==0
