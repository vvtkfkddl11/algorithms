import sys

n = int(sys.stdin.readline())
colors = str(sys.stdin.readline().strip())
min_cnt = 0
blues = 0
reds = 0
flag = 0 # 0이면 blue 1이면 red
if colors[0] == 'B':
    flag = 0
    blues += 1
else:
    flag = 1
    reds += 1

for i in colors:
    if i == 'B':
        if flag == 1:
            flag = 0
            blues += 1
    else:
        if flag == 0:
            flag = 1
            reds += 1

min_cnt = min(blues, reds) + 1  # 한 색으로 모두 칠하는 경우 더함
# print(blues, reds)
print(min_cnt)