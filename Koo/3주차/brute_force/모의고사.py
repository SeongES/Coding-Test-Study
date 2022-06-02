def solution(answers):
    answer = []
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]
    
    for i, ans in enumerate(answers) :
        if ans == answer_1[i % len(answer_1)]:
            correct[0] += 1
        if ans == answer_2[i % len(answer_2)]:
            correct[1] += 1
        if ans == answer_3[i % len(answer_3)]:
            correct[2] += 1
            
    for i, item in enumerate(correct) :
        if item == max(correct):
            answer.append(i+1)
    
    return answer
