n, m = map(int, input().split())
stack = []


def dfs(start):
    for i in range(start, n+1):  # 1, 2 / 1, 3
        if i not in stack:  # 이 조건의 존재 이유는?
            stack.append(i)
            dfs(i+1)  # 중간에 넣는 이유는?
            stack.pop()
            # arr.append(stack)

    if len(stack) == m:
        print(' '.join(map(str, stack)))


dfs(1)  # start = 1 로 초기화