# 11659 구간 합 구하기

import sys
input = sys.stdin.readline

numberOfData, numberOfLines = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for j in range(numberOfLines):
    numI, numJ = map(int, input().split())
    print(prefix_sum[numJ]-prefix_sum[numI-1])