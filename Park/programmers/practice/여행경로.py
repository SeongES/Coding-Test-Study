from collections import defaultdict # dictionary value의 default 자료구조 설정.

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys(): # ??value는 하나인데 정렬?
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        # stack에 저장 후 answer에 역순('ICN' ~)으로 저장.
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer
