import sys
from itertools import combinations

target = str(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
books = []

for i in range(n):
    price, name = map(str, sys.stdin.readline().split())
    books.append([int(price), name])

min_cost = float('inf')
can_make = True

for i in range(1, n+1):
    for j in combinations(range(n), i):
        chars = ""
        cur_cost = 0
        for k in j:
            chars += books[k][1]
        can_make = True
        for k in target:
            if chars.count(k) < target.count(k):
                can_make = False
                break
        if can_make:
            for k in j:
                cur_cost += books[k][0]
            min_cost = min(min_cost, cur_cost)

if can_make:
    print(min_cost)
else:
    print(-1)