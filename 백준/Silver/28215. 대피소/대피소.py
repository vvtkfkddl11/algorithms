import sys
from itertools import combinations


n, k = map(int, sys.stdin.readline().split())
homes = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    homes.append([x, y])
shelters = []
min_v = 1e9

for i in combinations(homes, k):
    max_distance = 0
    for x2, y2 in homes:
        min_distance = 1e9
        for j in i:
            x1, y1 = j
            min_distance = min(min_distance, abs(x1 - x2) + abs(y1 - y2))
        max_distance = max(max_distance, min_distance)
    min_v = min(min_v, max_distance)
    
print(min_v)