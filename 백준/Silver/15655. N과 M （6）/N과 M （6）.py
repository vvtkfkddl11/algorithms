import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums = sorted(nums)

answer = list(combinations(nums, m))

for i in answer:
    print(*i)