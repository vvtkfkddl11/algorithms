n, m = map(int, input().split())
stack = []


def dfs():
    for i in range(1, n+1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()

    if len(stack) == m:
        print(' '.join(map(str, stack)))  # 베열 출력 시 대괄호 없애기!


dfs()