def solution(t, p):
    answer = 0
    pLength = len(p)
    newStr = []
    count = 0
    for i in range(len(t)):
        newStr.append(t[i:i + pLength])
        if len(newStr[-1]) < pLength:
            newStr.pop()
            break
        # print(newStr)

    for char in newStr:
        if char <= p:
            count += 1
    answer = count
    return answer