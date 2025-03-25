import sys

n = int(sys.stdin.readline())


def make(n):
    # DP 테이블 초기화
    dp = [0] * (n + 1)
    dp[1] = 0

    # 작은 문제부터 차례로 해결
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)

    return dp[n]


print(make(n))