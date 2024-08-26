from collections import deque

def solution(t, p):
    answer = 0
    queue = deque()
    p_len = len(p)
    
    for i in str(t):
        queue.append(i)
        if len(queue) == p_len:
            # 현재 queue에 저장된 문자열을 정수로 변환하여 비교
            temp = ''.join(queue)
            if int(temp) <= int(p):
                answer += 1
            # queue에서 첫 번째 문자를 제거
            queue.popleft()
    
    return answer

# def solution(t, p):
#     answer = 0
#     temp = ''
#     for i in str(t):
#         temp += i
#         if len(temp) == len(p):
#             if int(temp) <= int(p):
#                 answer += 1
#             temp = temp[1:]
#     return answer