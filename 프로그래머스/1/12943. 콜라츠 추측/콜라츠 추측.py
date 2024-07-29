def dfs(count, num):
    if count == 500:
        return -1
    if num == 1:
        return count
    else:
        count += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        return dfs(count, num)

def solution(num):
    answer = 0
    count = 0
    answer = dfs(count, num)
    return answer