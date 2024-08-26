from itertools import permutations

def solution(before, after):
    answer = 1

    temp = {}
    for i in after:
        temp[i] = 0
    for i in after:
        temp[i] += 1
    for i in before:
        if i in temp:
            temp[i] -= 1
    print(temp)
    for i in temp:
        if temp[i] != 0:
            answer = 0
    return answer


    # temp = []
    # for i in before:
    #     temp.append(i)

#     for i in before:
#         # print(i)
#         if i in after:
#             after = after.strip(i)  # 하나만 제거
#             # print(after)
        
#     if after == "":
#         answer = 1

    # print(temp)
    # temp = list(map(''.join,permutations(before)))
    # if after in temp:
    #     answer = 1