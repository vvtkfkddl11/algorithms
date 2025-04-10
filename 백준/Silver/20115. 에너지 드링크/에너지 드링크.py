import sys


n = int(sys.stdin.readline())
drinks = list(map(int, sys.stdin.readline().split()))

max_v = max(drinks)
result = max_v + (sum(drinks) - max_v)/2

if result.is_integer():
    print(int(result))
else:
    print(result)