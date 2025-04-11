import sys


s = str(sys.stdin.readline().strip())
k = str(sys.stdin.readline().strip())

stack = []
k_len = len(k)

for char in s:
    stack.append(char)

    # 스택의 끝 문자가 폭발 문자열의 끝 문자와 같고, 스택의 크기가 충분하다면
    if char == k[-1] and len(stack) >= k_len:
        # 스택의 끝부분이 폭발 문자열과 일치하는지 확인
        if ''.join(stack[-k_len:]) == k:
            # 폭발 문자열 길이만큼 스택에서 제거
            for _ in range(k_len):
                stack.pop()

result = ''.join(stack)
if not result:
    print("FRULA")
else:
    print(result)