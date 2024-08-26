def solution(n):
    answer = 0
    n = str(n)
    temp = {}
    temp2 = ''
    for i in range(9, -1, -1):
        temp[i] = 0
    for i in n:
        temp[int(i)] += 1
    # print(temp)
    for a, b in temp.items():
        for i in range(b):
            temp2 += str(a)
            
    answer = int(temp2)
    return answer

#     n = str(n)
#     # temp = ''
#     temp = n[0]
#     print(temp)
    
#     for i in range(1, len(n)):
#         if int(temp[i-1]) > int(n[i]):
#             temp += temp[i-1]
#             # temp[i-1] = n[i]
#         else:
#             temp += n[i]
#         print(''.join(temp))