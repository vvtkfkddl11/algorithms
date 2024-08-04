import sys

n = int(sys.stdin.readline())
temp = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    temp.append([a, b])
temp.sort()
for i in temp:
    print(*i)