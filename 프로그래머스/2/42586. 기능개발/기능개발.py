import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    temp = math.ceil((100 - progresses[0])/speeds[0])
    cnt = 0
    visited = [0]*(len(progresses)) # 완료1/미완료0 상태를 담은 배열
    while sum(visited)<len(visited):
        for i in range(len(progresses)):
            progresses[i] += temp*speeds[i]
        for i in range(len(progresses)):
            if progresses[i] >= 100 and visited[i] == 0:
                cnt += 1
                visited[i] = 1
            if progresses[i] < 100:
                temp = math.ceil((100 - progresses[i])/speeds[i])
            if visited[i] == 0 and cnt > 0:
                answer.append(cnt)
                cnt = 0
                break
    if cnt > 0: 
        answer.append(cnt)
    return answer