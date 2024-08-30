
import sys

k, n = map(int, sys.stdin.readline().split())
arr = []
sum_k = 0
for i in range(k):
    a = int(sys.stdin.readline())
    arr.append(a)
    sum_k += a

start = 1
end = sum_k // n

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in arr:
        temp += i // mid
        
    if temp >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)