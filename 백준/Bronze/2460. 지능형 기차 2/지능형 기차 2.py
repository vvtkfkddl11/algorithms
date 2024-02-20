# 지능형 기차 2

arr = [list(map(int, input().split())) for _ in range(10)]
summ = 0
record = []

for i in range(len(arr)):
    summ += (arr[i][1]-arr[i][0])
    record.append(summ)

record.sort()
print(record[-1])