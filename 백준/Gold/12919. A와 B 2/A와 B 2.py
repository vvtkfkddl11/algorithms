import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
result = 0


def dfs(t):
    global result

    if t == s:  # s문자열과 같아졌을 때환1 반환
        result = 1
        return

    if len(t) == 0:  # s문자열과 같아지는 조건을 건너뛰고 0이 됨 -> 0 반
        return

    if t[-1] == 'A':    # 마지막 문자가 A일 때, 마지막 인덱스 제외하고 돌기
        dfs(t[:-1])  # t[:-1]: 마지막 문자를 제외한 모든 문자 선택
        
    if t[0] == 'B':
        dfs(t[1:][::-1])  # t[::-1]: 문자열 뒤집기


dfs(t)
print(result)