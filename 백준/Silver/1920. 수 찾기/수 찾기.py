import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a_dict = {a[i]: 0 for i in range(n)}

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
for key in b:
    if key in a_dict:
        print(1)
    else:
        print(0)