import sys

n, k = map(int, sys.stdin.readline().split())


def solution(n, k):
    min_sum = k * (k + 1) // 2  # 등차수열 공식: 1부터 k까지의 합
    if min_sum > n:
        return - 1
    elif (n-min_sum) % k == 0:
        return k - 1
    else:
        return k


print(solution(n, k))