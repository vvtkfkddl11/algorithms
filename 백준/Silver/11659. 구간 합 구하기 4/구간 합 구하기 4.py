import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))
sums = []
temp = 0
sums.append(temp)

for i in numbers:
    temp += i
    sums.append(temp)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sums[b]-sums[a-1])