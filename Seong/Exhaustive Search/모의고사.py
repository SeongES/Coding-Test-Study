def solution(answers):
    answer = []
    stud_1 = [1,2,3,4,5]
    stud_2 = [2,1,2,3,2,4,2,5]
    stud_3 = [3,3,1,1,2,2,4,4,5,5]
    cnt_1, cnt_2, cnt_3 = 0,0,0
    cor =[]
    for i in range(len(answers)):
        if stud_1[i%len(stud_1)] == answers[i] :
            cnt_1 +=1
        if stud_2[i%len(stud_2)] == answers[i] :
            cnt_2 +=1
        if stud_3[i%len(stud_3)] == answers[i] :
            cnt_3 +=1

    # print(cnt_1, cnt_2, cnt_3)
    cor.append(cnt_1)
    cor.append(cnt_2)
    cor.append(cnt_3)

    for i in range(len(cor)):
        if max(cor) == cor[i]:
            answer.append(i+1)
    # answer =np.argmax(answer) +1
    # answer = 
    return answer
