'''
출처 : https://doraeul19.tistory.com/m/201
- 풀이
1. 2배 크기의 배열 선언(상자들이 인접할때, 넘어가는 것을 막기 위해)
2. 1은 이동 가능한곳, 0은 이동 불가능한곳, 2는 아이템의 위치이다.
3. 먼저 모든 직사각형의 테두리를 그린다.
4. 모든 직사각형에 대해 테두리를 제외한 나머지 부분은 0으로 채운다.
5. 캐릭터 시작위치, 아이템 위치를 넣어준다.
6. 순차적으로 탐색...
  - 시작위치에서 탐색을 시작해, 다시 시작위치로 돌아오는 길이를 구한다.
  - 시작위치 ▶ 아이템위치 ▶ 시작위치, 아이템있는 곳에 도착하면, result에 시작위치 ▶ 아이템위치까지의 길이를 저장한다.
7. 루프가 끝나면, 둘 중 최솟값 반환
'''
import numpy as np
def solution(rectangle, characterX, characterY, itemX, itemY):
    SIZE = 51
    arr = np.zeros((SIZE*2, SIZE*2))
    for r in rectangle: #사각형 칠하기
        arr[r[1]*2-1:r[3]*2, r[0]*2-1:r[2]*2] = 1
    for r in rectangle: #사각형 테두리 제외하고 칠하기
        arr[r[1]*2:r[3]*2-1, r[0]*2:r[2]*2-1] = 0
    x, y = characterX*2-1, characterY*2-1   #캐릭터 시작위치
    arr[y][x] = 0
    arr[itemY*2-1][itemX*2-1] = 2   #아이템 위치
    temp, result = 0, 0
    while True:
        temp += 1
        if arr[y][x+1] > 0:    #우
            x = x+1
        elif arr[y][x-1] > 0:    #좌
            x = x-1
        elif arr[y-1][x] > 0:    #하
            y = y-1
        elif arr[y+1][x] > 0:   #상
            y = y+1
        else:
            break
        if arr[y][x] == 2:  #현재 위치가 아이템이면
            result = temp
        arr[y][x] = 0
    return min(result, temp-result)//2
