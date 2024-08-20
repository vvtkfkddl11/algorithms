import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1)
# dp[i]: i에서 1로 만드는 데 걸리는 최소 연산 횟수

dp[1] = 0  # 1일 때 연산 불필요

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])