def solution(numbers):
    answer = ''
    temp = list(map(str, numbers))
    answer = sorted(temp, key = lambda x: x*3, reverse = True)
    # str -> int -> str (0으로만 이루어진 경우 대비)
    return str(int(''.join(answer)))

# def dfs(n):
#     if len(n) == 1:
#         break
#     temp =
    
# temp = {}

#     for i in numbers:
#         if len(i) == 1:
#             if i not in temp:
#                 temp[i] = 1
#             else:
#                 temp[i] += 1
                
    # print(temp)
# temp = {}
    # temp = ''
    # temp2 = []
    # for i in numbers:
    #     temp += str(i)
    # temp2 = list(temp)
    # print(temp2)
    # temp2.sort(reverse = True)
    # answer = ''.join(temp2)