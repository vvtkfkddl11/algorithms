from itertools import permutations

def solution(k, dungeons):
    answer = 0
    new = list(permutations(dungeons, len(dungeons)))
    temp = [list(item) for item in new]
    arr = []
    max_cnt = 0
    for i in range(len(temp)):
        cnt = 0
        cur_k = k
        for j in range(len(temp[0])):
            if cur_k >= temp[i][j][0]:
                cur_k -= temp[i][j][1]
                cnt += 1
                # print(cur_k, temp[i][j][0], temp[i][j][1])
                # print("cnt: ", cnt)
            else:
                break   
        max_cnt = max(max_cnt, cnt)
    return max_cnt