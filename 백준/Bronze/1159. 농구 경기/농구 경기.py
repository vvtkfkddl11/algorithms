import sys

n = int(sys.stdin.readline().strip())
names = {}
answer = []

for i in range(n):
    name = str(sys.stdin.readline().strip())
    if name[0] in names:
        # print(names)
        # print("있음", name)
        names[name[0]] += 1
        if names[name[0]] == 5:
            # print("5와 같")
            answer.append(name[0])
    else:
        # print(names)
        # print("없음", name)
        names[name[0]] = 1

# print(names)
# print(answer)

if len(answer) == 0:
    print("PREDAJA")
else:
    answer.sort()
    print(''.join(answer))