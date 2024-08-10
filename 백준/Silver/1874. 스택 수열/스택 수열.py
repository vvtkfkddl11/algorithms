import sys

n = int(sys.stdin.readline())
stack = []
answer = []
current_num = 1
flag = 0  # 가능/불가능 여부

for i in range(n):
    num = int(sys.stdin.readline())

    while current_num <= num:
        stack.append(current_num)
        answer.append("+")
        current_num += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        flag = 1
        print("NO")
        break

if flag != 1:
    for i in answer:
        print(i)