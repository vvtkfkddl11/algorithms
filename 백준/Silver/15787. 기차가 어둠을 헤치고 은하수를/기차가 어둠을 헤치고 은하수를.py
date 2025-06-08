import sys

n, m = map(int, sys.stdin.readline().split())
trains = [[0]*20 for _ in range(n)]

def command1(commands):
    trains[commands[1]-1][commands[2]-1] = 1

def command2(commands):
    trains[commands[1]-1][commands[2]-1] = 0
    return

def command3(commands):
    for i in range(20-1, 0, -1):
        trains[commands[1]-1][i] = trains[commands[1]-1][i-1]
    trains[commands[1]-1][0] = 0
    return

def command4(commands):
    for i in range(20-1):
        trains[commands[1]-1][i] = trains[commands[1]-1][i+1]
    trains[commands[1]-1][-1] = 0
    return

for i in range(m):
    commands = list(map(int, sys.stdin.readline().split()))
    if commands[0] == 1:
        command1(commands)
    elif commands[0] == 2:
        command2(commands)
    elif commands[0] == 3:
        command3(commands)
    elif commands[0] == 4:
        command4(commands)

print(len(set(tuple(x) for x in trains)))