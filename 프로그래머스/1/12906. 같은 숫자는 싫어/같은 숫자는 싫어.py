def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a


# from collections import deque

# def solution(arr):
#     answer = []
#     queue = deque(arr)
#     x = queue.popleft()
#     answer.append(x) 
#     while queue:
#         nx = queue.popleft()
#         if x != nx:
#             answer.append(nx) 
#         if queue:
#             x = nx
            
#     return answer