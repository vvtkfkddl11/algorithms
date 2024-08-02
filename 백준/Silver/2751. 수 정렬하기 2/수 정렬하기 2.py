import sys

n = int(sys.stdin.readline())
temp = []
for i in range(n):
    a = int(sys.stdin.readline())
    temp.append(a)
temp.sort()
for i in temp:
    print(i)