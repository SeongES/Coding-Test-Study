def solution(brown, yellow):
    answer = []
    
    div_list = divisor(yellow)
    print(div_list)
     
    for i, item in enumerate(div_list) :
        if i >= len(div_list) / 2 :
            break
        
        w, h = item, yellow / item
        if h > w : w , h = h, w
        
        cal_b = (w + 2) * 2 + (h + 2) * 2 - 4
        
        if cal_b == brown :
            answer = [w + 2, h + 2]
    
    return answer

def divisor(num) :
    div = []
    
    for i in range(1, num + 1) :
        if num % i == 0 :
            div.append(i)
            
    return div
