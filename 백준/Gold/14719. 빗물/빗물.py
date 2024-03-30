h, w = map(int, input().split())  # 4 8
m = list(map(int, input().split()))  # 3 1 2 3 4 1 1 2
result = 0
for i in range(1, w-1):  # 3 6 2 3 4 1 1 2
    r = max(m[:i])
    l = max(m[i+1:])
    # print(m[i])
    if m[i] < min(r, l):
        result += min(r, l) - m[i]

print(result)