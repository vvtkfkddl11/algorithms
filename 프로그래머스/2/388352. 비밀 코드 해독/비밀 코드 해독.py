from itertools import combinations


def solution(n, q, ans):
    answer = 0

    tmp = list(combinations((i for i in range(1, n+1)), 5))
    candidates = []

    for i in tmp:
        candidates.append(list(i))

    m = len(q)

    for i in candidates:
        cur_ans = 0
        common = []
        for j in range(m):
            cur_ans = len(set(i) & set(q[j]))

            if cur_ans == ans[j]:
                common.append(cur_ans)
            else:
                break
        if common == ans:
            answer += 1

    return answer