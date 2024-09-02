import sys

n, m = map(int, sys.stdin.readline().split())
dic = {i: set() for i in range(1, n+1)}  # 기차의 좌석 상태를 저장할 딕셔너리

for _ in range(m):
    command = sys.stdin.readline().strip().split()
    train_idx = int(command[1])
    
    if command[0] == '1':  # 좌석에 사람을 태움
        dic[train_idx].add(int(command[2]))
    elif command[0] == '2':  # 좌석에서 사람을 내림
        dic[train_idx].discard(int(command[2]))
    elif command[0] == '3':  # 모든 승객을 뒤로 한 칸 이동
        dic[train_idx] = {x + 1 for x in dic[train_idx] if x < 20}
    elif command[0] == '4':  # 모든 승객을 앞으로 한 칸 이동
        dic[train_idx] = {x - 1 for x in dic[train_idx] if x > 1}

# 고유한 기차 상태를 찾기 위한 집합
unique_trains = set()

for i in range(1, n + 1):
    state = tuple(sorted(dic[i]))  # 집합을 튜플로 변환해 순서 상관없이 비교
    unique_trains.add(state)

print(len(unique_trains))
