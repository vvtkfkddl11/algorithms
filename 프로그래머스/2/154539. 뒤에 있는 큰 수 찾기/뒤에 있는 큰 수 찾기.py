def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    while stack:
        answer[stack.pop()] = -1
        
    return answer


'''
시간초과

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        flag = 0    
        for j in numbers[i+1:]:
            if j > numbers[i]:
                answer.append(j)
                flag = 1
                break
        if flag == 0:
            answer.append(-1)
    return answer
'''