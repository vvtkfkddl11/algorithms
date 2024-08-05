import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
people = deque()
answer = []

for i in range(1, n+1):
    people.append(i)
while people:
    for i in range(k-1):
        people.append(people.popleft())
    answer.append(people.popleft())

print(str(answer).replace("[", "<").replace("]", ">"))