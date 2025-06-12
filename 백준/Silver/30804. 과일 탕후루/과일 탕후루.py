import sys
from collections import defaultdict

n = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))

fruit_cnt = defaultdict(int)
left = 0
max_len = 0

for right in range(n):
    fruit_cnt[fruits[right]] += 1
    while len(fruit_cnt) > 2:
        fruit_cnt[fruits[left]] -= 1
        if fruit_cnt[fruits[left]] == 0:
            del fruit_cnt[fruits[left]]
        left += 1
    max_len = max(max_len, right - left + 1)
    
print(max_len)