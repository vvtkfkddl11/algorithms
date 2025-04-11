import sys


n = int(sys.stdin.readline())
files = {}
for i in range(n):
    s = sys.stdin.readline().strip()
    file = s.split(".")[-1]
    if file not in files:
        files[file] = 1
    else:
        files[file] += 1
answer = sorted(files.items())
for key, value in answer:
    print(key, value)