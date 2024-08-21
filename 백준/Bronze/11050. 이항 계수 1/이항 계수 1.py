import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(0, n+1):
    dp[i][1] = i  # 5C1
    dp[i][0] = 1  # 5C0
    dp[i][i] = 1  # 5C1

for i in range(0, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]  

print(dp[n][k])