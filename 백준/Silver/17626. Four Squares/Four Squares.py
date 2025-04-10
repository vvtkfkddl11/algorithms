# DP - Python3 시간초과
import sys
import math

n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[1] = 1   # 1 = 1^2 -> 1개

for i in range(2, n+1):
    min_v = 1e9
    for j in range(1, int(math.sqrt(i))+1):
        # i보다 작은 제곱수(j**2)를 뺀 나머지 값에 대한 최소 제곱수 개수 + 1
        min_v = min(min_v, dp[i-j**2])
    dp[i] = min_v + 1   # +1은 현재 사용한 제곱수 j²를 추가한 것

print(dp[n])