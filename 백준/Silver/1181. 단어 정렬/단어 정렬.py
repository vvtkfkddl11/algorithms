import sys

n = int(sys.stdin.readline())
strings = []
for i in range(n):
    a = str(sys.stdin.readline().strip())
    if a in strings:
        continue
    strings.append(a)
# 간소화: strings.extend([str(sys.stdin.readline().strip()) for _ in range(n)])

strings.sort()
strings.sort(key=len)

for i in strings:
    print(i)