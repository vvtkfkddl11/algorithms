import sys

n, m = map(int, sys.stdin.readline().split())
names = {}


# 간략화 방법 찾기
for i in range(n):
    name = str(sys.stdin.readline().strip())
    names[i+1] = name  # 딕셔너리에 인덱스-이름 저장
    names[name] = i+1


for i in range(m):
    input = sys.stdin.readline().strip()
    if input[0].isupper():  # 대문자라면 - 문자일 때
        input = str(input)
        print(names[input])
    else:
        input = int(input)  # 숫자일 때
        print(names[input])

   