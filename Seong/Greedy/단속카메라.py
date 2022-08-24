
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 차량 진출 시점으로 sort 오름차순
    camera = -30001 # 진입 시점 init
    print(routes)
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1] # 진출 시점으로 재설정
    return answer

  # https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/
