def solution(t, p):
    answer = 0
    temp = ''
    for i in str(t):
        temp += i
        if len(temp) == len(p):
            if int(temp) <= int(p):
                answer += 1
            temp = temp[1:]
    return answer