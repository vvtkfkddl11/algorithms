import sys


n = int(sys.stdin.readline())
stairs = [0]

for i in range(n):
    stairs.append(int(sys.stdin.readline()))

# dp[0]은 아직 어떤 계단도 밟지 않은 상태 => 점수 0점
dp = [0] * (n+1)

# 초기 설정
if n >= 1:
    dp[1] = stairs[1]
if n >= 2:
    dp[2] = stairs[1] + stairs[2]

for i in range(3, n+1):
    # 두 가지 경우 중 최댓값 선택:
    # 1. i-2번째 계단에서 i번째 계단으로 바로 오는 경우
    # 2. i-3번째 계단에서 i-1번째 계단을 거쳐 i번째 계단으로 오는 경우
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    
print(dp[n])