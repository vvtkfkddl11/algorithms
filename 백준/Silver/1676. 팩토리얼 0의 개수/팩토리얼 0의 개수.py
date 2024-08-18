import sys
n = int(sys.stdin.readline())
cnt = 0


def factorial(num):
    if num > 0:
        return num*factorial(num-1)
    else:
        return 1


result = factorial(n)
result = str(result)
# print(str(result).count("0"))

for i in range(len(result)-1, -1, -1):
    if result[i] == "0":
        cnt += 1
    else:
        break

print(cnt)