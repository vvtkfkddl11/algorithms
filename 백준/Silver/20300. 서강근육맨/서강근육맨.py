import sys
from collections import deque

n = int(sys.stdin.readline())
ts = list(map(int, sys.stdin.readline().split()))
max_sum = 0

ts.sort()
# print(ts)
d = deque(ts)

if n % 2 == 0:
    max_sum = d[0] + d[-1]
    d.popleft()
    d.pop()
else:
    max_sum = d[-1]
    d.pop()

# print(d)

while d:
    current_sum = d[0] + d[-1]
    max_sum = max(max_sum, current_sum)
    d.popleft()
    d.pop()
    
print(max_sum)