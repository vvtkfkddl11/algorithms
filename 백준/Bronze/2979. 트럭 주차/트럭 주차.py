costs = list(map(int, input().split()))
times = [list(map(int, input().split())) for _ in range(3)]

maxTime = max(times, key=lambda item: item[1])[1]
arr = [0]*maxTime
nowTime = 0
result = 0

for i in times:
    for j in range(i[0], i[1]):
        arr[j] += 1

for i in arr:
    if i == 1:
        result += costs[0]
    elif i == 2:
        result += (2*costs[1])
    elif i == 3:
        result += (3*costs[2])

print(result)