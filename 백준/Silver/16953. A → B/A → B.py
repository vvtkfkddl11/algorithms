import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())


def method1(num):
    return num*2


def method2(num):
    return int(str(num)+'1')


queue = deque([[a, 1]])  # 숫자랑, 횟수 추가

while queue:
    num, cnt = queue.popleft()
    if num == b:
        print(cnt)
        break
    if method1(num) <= b:
        queue.append([method1(num), cnt+1])
    if method2(num) <= b:
        queue.append([method2(num), cnt+1])
else:
    print(-1)