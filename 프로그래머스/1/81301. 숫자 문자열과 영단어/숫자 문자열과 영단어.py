def solution(s):
    answer = ''
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    temp = ''
    for i in s:
        if ord(i) >= 48 and ord(i) <= 57:
            answer += i
        else:
            temp += i
            if temp in dic:
                answer += str(dic[temp])
                temp = ''
    return int(answer)

# def solution(s):
#     answer = 0
#     num_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
#     num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#     temp = ''
#     tempStr = ''
#     for i in s:
#         if i in num:
#             if tempStr != '':  
#                 temp += num_dic[tempStr]
#                 tempStr = ''
#             temp += i
#         else:
#             tempStr += i
#             if tempStr in num_dic:
#                 temp += num_dic[tempStr]
#                 tempStr = ''   
#     answer = int(temp)  
#     return answer