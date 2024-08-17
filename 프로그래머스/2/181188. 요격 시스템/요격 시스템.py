def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    end = 0
    for i in targets:
        if i[0] >= end:
            answer += 1
            end = i[1]
    return answer