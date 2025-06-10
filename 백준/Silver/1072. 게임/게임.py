import sys

X, Y = map(int, sys.stdin.readline().split())
answer = -1
left, right = 0, X
z = (Y * 100) // X

if X == Y:
     print(answer)
else:
    while left <= right:
        mid = (left+right) // 2
        new_z = ((Y+mid)*100) // (X+mid)
        if new_z != z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)