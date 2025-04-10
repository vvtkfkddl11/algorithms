import sys
import math


n = int(sys.stdin.readline())

# 제곱수 체크
def is_square(num):
    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else:
        return False

min_v = 4   # 최대 개수가 4개

# 하나의 제곱수의 합인 경우 (n 자체가 제곱수)
if is_square(n):
    min_v = 1
else:
    for i in range(int(math.sqrt(n)), 0, -1):   # 숫자 n의 제곱근부터 1까지 역순으로 반복
        # 두 제곱수의 합인 경우
        if is_square(n-(i**2)):
            min_v = 2
            break
        else:
            for j in range(int(math.sqrt(n-i**2)), 0, -1):
                # 세 제곱수의 합인 경우
                if is_square(n-(i**2)-(j**2)):
                    min_v = 3
                    break
print(min_v)
