def solution(s):
    answer = 0
    stack = []
    s = s.split(" ")
    print(stack)
    
    for i in s:
        if i == 'Z':
            stack.pop()
        else:
            i = int(i)
            stack.append(i)
    for i in stack:
        answer += int(i)
    
    return answer