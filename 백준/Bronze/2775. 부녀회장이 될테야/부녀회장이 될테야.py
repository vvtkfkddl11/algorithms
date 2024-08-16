import sys

t = int(sys.stdin.readline())

for i in range(t):
    cur = 0

    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    arr = [i for i in range(1, n + 1)]

    for _ in range(k):  # k층까지 계산
        for j in range(1, n):
            arr[j] += arr[j - 1]  # 현재 층의 각 호수 계산

    print(arr[-1])  # k층 n호 사람 수 출력