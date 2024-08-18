import sys
n = int(sys.stdin.readline())
cnt = 0
i = 5

while n >= i:
    cnt += n // i
    i *= 5
print(cnt)