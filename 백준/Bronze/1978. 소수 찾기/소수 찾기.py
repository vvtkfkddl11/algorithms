import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

answer = 0


def isPrime(n):
    if n <= 1:  # 1보다 작거나 같은 수는 소수가 아님
        return False
    for i in range(2, int(n**(1/2)+1)):  # 2부터 n의 제곱근까지 반복
        if n % i == 0:  # n이 i의 배수이면 소수가 아님
            return False
    return True


for i in numbers:
    if isPrime(i):
        answer += 1

print(answer)