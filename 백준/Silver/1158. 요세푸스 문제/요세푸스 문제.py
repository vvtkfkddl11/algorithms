import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
people = deque()
result = []
for i in range(1, n+1):
    people.append(i)

while people:
    for i in range(k-1):
        people.append(people.popleft())  # 0부터 k-1번째 요소 제거 후 people에 추가
    result.append(people.popleft())  # k번째 요소 제거 후 result에 추가
print(str(result).replace('[', '<').replace(']', '>'))