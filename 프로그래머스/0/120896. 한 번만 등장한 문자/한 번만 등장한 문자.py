def solution(s):
    answer = ''
    temp = {}
    for i in s:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] += 1
    temp = dict(sorted(temp.items()))
    for a, b in temp.items():
        if b == 1:
            answer += a
    return answer