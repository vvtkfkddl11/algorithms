import sys

h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
graph = []

for i in range(n):
    r, c = map(int, sys.stdin.readline().split())
    graph.append([r, c])

max_size = 0
r, c = graph[0]

for i in range(n):
    r1, c1 = graph[i]
    for j in range(i+1, n):
        r2, c2 = graph[j]

        if (r1+r2<=h and max(c1, c2)<=w) or (c1+c2<=w and max(r1, r2)<=h):
            max_size = max(max_size, (r1*c1 + r2*c2))

        if (r1+c2<=h and max(r2, c1)<=w) or (r2+c1<=w and max(r1, c2)<=h):
            max_size = max(max_size, (r1*c1 + r2*c2))

        if (r2+c1<=h and max(r1, c2)<=w) or (r1+c2<=w and max(r2, c1)<=h):
            max_size = max(max_size, (r1*c1 + r2*c2))

        if (c1+c2<=h and max(r1, r2)<=w) or (r1+r2<=w and max(c1, c2)<=h):
            max_size = max(max_size, (r1*c1 + r2*c2))

        else:
            continue

print(max_size)