import sys

n = int(sys.stdin.readline())
temp = []
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    temp.append((a, b))

temp.sort(key=lambda x : x[0])

for i in temp:
    print(*i)