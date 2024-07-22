def solution(lottos, win_nums):
    answer = []
    rank = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2}  # 순위, 당첨 일치 개수
    count = 0
    count_zero = 0
    max_rank = 0
    min_rank = 0

    for i in lottos:
        if i in win_nums:
            count += 1
        if i == 0:
            count_zero += 1

    for a, b in rank.items():
        if b == count+count_zero:
            max_rank = a

    for a, b in rank.items():
        if b == count:
            min_rank = a
            
    if count < 2:
        print("hi")
        min_rank = 6
    
    if count+count_zero < 2:
        max_rank = 6
        
    answer.append(max_rank)
    answer.append(min_rank)
    
    return answer