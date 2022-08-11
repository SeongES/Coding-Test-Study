import heapq

def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)
    jobs = sorted(jobs, key = lambda x : x[1])
    
    while len(jobs) :
        for i, job in enumerate(jobs) :
            if job[0] <= time :
                time += job[1]
                answer += time - job[0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1 :
                time += 1
    return answer // n
