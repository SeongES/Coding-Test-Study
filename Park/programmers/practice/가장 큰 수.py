def solution2(numbers):
    answer = ''
    len_=[]
    temp=[]
    dic={}
    for number in numbers:
        s_number=str(number)
        value=len(s_number)
        key = (s_number*4)[:4]
        try:
            if str(key) in dic.keys():
                dic_value=[dic[key]]
                dic_value.append(value)
                dic[key]=dic_value
            else:
                dic[key]=value
        except:
            dic[key]=value
    sorted_dict = sorted(dic.items(), key = lambda item: item[0], reverse = True)
    for (i,j) in sorted_dict:
        if type(j)!=int:
            for jj in j:
                answer+=i[0:jj]
        else:
            answer+=i[0:j]
    return answer
