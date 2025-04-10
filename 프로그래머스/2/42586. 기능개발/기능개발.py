import math


def solution(progresses, speeds):
    answer = []
    cnt = 0
    required = []
    for i in range(len(progresses)):
        required.append(math.ceil((100-progresses[i])/speeds[i]))
    max_days = required[0]
    for i in required:
        if i > max_days:
            answer.append(cnt)
            cnt = 1
            max_days = i
        else:
            cnt += 1
    if cnt > 0:
        answer.append(cnt)
    return answer