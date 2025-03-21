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


# from itertools import permutations

# def solution(n, q, ans):
#     answer = 0
#     tmp = []
#     for i in range(1, n+1):
#         tmp.append(i)
#     # print(tmp)
#     a = list(permutations(tmp, 5))
#     print(a)
    
#     return answer

'''
numbers = []
    for i in range(1, n+1):
        numbers.append(i)
    combi = list(itertools.combinations(numbers, 5))
    candi = []
    for i in combi:
        candi.append(list(i))
        
    # print(candi)
    
    for i in candi:
        for j in range(5):
            cnt = 0
            for w in q[j]:
                if w in i:
                    cnt += 1
            if cnt != ans[j]:
                continue
            else:
                answer += 1
'''