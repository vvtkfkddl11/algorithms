import sys


n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))
p = [0] * n

for i in range(k):
    for j in range(n):
        p[d[j]-1] = s[j]
    # s = p는 배열 참조(reference)가 복사되므로 틀림
    s = p[:]  # 방법1
    # s = list(p)  # 방법2
    # s = copy.copy(p)  # 방법3
print(*p)