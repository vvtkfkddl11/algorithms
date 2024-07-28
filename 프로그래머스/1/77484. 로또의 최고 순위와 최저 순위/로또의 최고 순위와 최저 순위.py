def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]  # 인덱스 0부터 6까지의 순위 (일치하는 숫자 개수에 따른 순위)

    count_win = sum(1 for i in lottos if i in win_nums)
    count_zero = sum(1 for i in lottos if i == 0)

    max_rank = rank[count_win + count_zero]
    min_rank = rank[count_win]

    return [max_rank, min_rank]
