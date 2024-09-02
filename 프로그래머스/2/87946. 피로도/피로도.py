from itertools import permutations

def solution(k, dungeons):
    answer = -1
    com = list(map(list, permutations(dungeons, len(dungeons))))
    # print(com)
    max_v = 0
    
    for i in range(len(com)):
        cur_k = k
        cnt = 0
        for j in range(len(com[i])):
            if cur_k >= com[i][j][0]:
                cur_k -= com[i][j][1]
                cnt += 1
            else:
                break
        max_v = max(max_v, cnt)
    
    return max_v