import sys


n = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

costs.pop()

min_cost = costs[0]
sum_cost = costs[0] * distances[0]

for i in range(1, len(costs)):
    min_cost = min(min_cost, costs[i])
    sum_cost += min_cost * distances[i]

print(sum_cost)