import sys

n = int(sys.stdin.readline())

cnt1 = 0
cnt2 = 0
dp = [0]*(n+1)

def fibo_recursive(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_dp(n):
    global dp
    global cnt2

    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        cnt2 += 1
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


fibo_recursive(n)
fibo_dp(n)
print(cnt1, cnt2)