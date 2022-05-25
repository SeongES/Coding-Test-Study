def solution(answers):
    X, Y, Z = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0]*3
    
    for idx, answer in enumerate(answers):
        if answer == X[idx%len(X)]:
            cnt[0] += 1
        if answer == Y[idx%len(Y)]:
            cnt[1] += 1
        if answer == Z[idx%len(Z)]:
            cnt[2] += 1
            
    answer = [i+1 for i in range(len(cnt)) if cnt[i] == max(cnt)]
    
    return print(answer)
solution([1,3,2,4,2])