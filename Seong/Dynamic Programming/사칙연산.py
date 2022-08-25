def solution(arr):
    tot_min, tot_max = 0,0
    sum_value = 0
    for idx in range(len(arr)-1, -1, -1): # 뒤에서부터 거꾸로 진행
        if arr[idx] == '+': # +는 쭉 더하기만
            continue

        elif arr[idx] == '-': # -에서 min max 경우 모두 계산
            tempmin, tempmax = tot_min, tot_max
            # minimum은 -val-max or -sum+min
            tot_min = min(-(sum_value + tempmax), -sum_value+tempmin)
            
            minus_v = int(arr[idx+1])
            print(minus_v)
            
            # maximum은 -val-min or -(-뒤에 있는것)+(나머지)
            tot_max = max(-(sum_value+tempmin), -minus_v+(sum_value-minus_v)+tempmax)
            print('sum', sum_value)
            # tot_max = max(-(sum_value+tempmin), -minus_v+(sum_value)+tempmax)

            sum_value = 0

        elif int(arr[idx]) >= 0: # 숫자 더하기
            sum_value += int(arr[idx])
    tot_max += sum_value
    return tot_max
