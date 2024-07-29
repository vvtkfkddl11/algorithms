def solution(new_id):
    answer = ''

    # level 1
    new_id = new_id.lower()
    print(new_id)

    # level 2
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer += i
    print(answer)

    # level 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    print("l3: ", answer)

    # level 4
    if len(answer) > 1:
        if answer[0] == '.':
            answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    # level 5
    if len(answer) == 0:
        answer += 'a'

    # level 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # level 7
    while len(answer) <= 2:
        answer += answer[-1]

    return answer

















# def solution(new_id):
#     answer = ''
    
#     # 1단계
#     new_id = new_id.lower()

#     # 2단계
#     for str in new_id:
#         if str.isalpha() or str.isdigit() or str == '-' or str == '_' or str == '.':
#             answer += str

#     # 3단계
#     while '..' in answer:
#         answer = answer.replace('..', '.')
    
#     # 4단계
#     if len(answer) > 1:
#         if answer[0] == '.':
#             answer = answer[1:]
#     if answer[-1] == '.':
#         answer = answer[:-1]

#     # 5단계
#     if answer == '':
#         answer = "a"

#     # 6단계
#     if len(answer) >= 16:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
    
#     # 7단계
#     while len(answer) <= 2:
#         answer += answer[-1]

#     return answer