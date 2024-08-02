import sys

n = int(sys.stdin.readline())
temp = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    temp.append([x, y])
temp.sort(key=lambda x :(x[1], x[0]))
for i in temp:
    print(*i)