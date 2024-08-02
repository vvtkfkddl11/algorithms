import sys

n = int(sys.stdin.readline())


def solution(n):
    cnt = 0
    temp = 666
    while True:
        if '666' in str(temp):
            cnt += 1
        if cnt == n:
            break
        temp += 1
    answer = temp
    return answer


print(solution(n))