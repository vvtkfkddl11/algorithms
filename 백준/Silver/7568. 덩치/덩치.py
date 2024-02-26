n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
scores = []

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count += 1
    scores.append(count+1)

for i in scores:
    print(i)
