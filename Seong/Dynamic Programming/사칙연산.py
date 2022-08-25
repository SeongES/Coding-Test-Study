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

'''
[출처] https://tiktaek.tistory.com/33
1. -를 만나기 전까지 sum을 계산하니 sum은 4가 됩니다. -> -4

2. 다음 -를 만난 경우에 sum은 6(3+1+2)이고 최대 최소를 계산해보면

    최소 : -(6+(-4))=-2 또는 -(6)+(-4)=-10   -> -10
    최대 : -(6+(-4))=-2 또는 -(3)+(1+2)+(-4)=-4   -> -2

3. 다음 -를 만난 경우에 sum은 8(3+5)이고 최대 최소를 계산하면

    최소 : -(8+(-2))=-6 또는 -(8)+(-10)=-18   -> -18
    최대 : -(8+(-10))=2 또는 -(3)+5+-2=0   -> 2
'''
