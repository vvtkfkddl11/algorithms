def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    # print(new_id)  # 1단계

    second = ''
    third = ''
    fourth = ''

    for str in new_id:
        if str.isalpha() or str.isdigit() or str == '-' or str == '_' or str == '.':
            answer += str
    # print(second)  # 2단계

    while '..' in answer:
        answer = answer.replace('..', '.')
    # print(third)  # 3단계
    
    if len(answer) > 1:
        if answer[0] == '.':
            answer = answer[1:]
        else: 
            '.'
    
    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)  # 4단계

    if answer == '':
        answer = "a"
    # print(third)  # 5단계

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # print(third)  # 6단계

    while len(answer) <= 2:
        answer += answer[-1]

    return answer