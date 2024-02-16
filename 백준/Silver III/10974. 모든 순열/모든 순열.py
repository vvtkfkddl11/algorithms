import itertools
N = int(input())
answer = []


def fac(n):
    for i in range(1, n+1):
        answer.append(i)


fac(N)

for i in itertools.permutations(answer):
    print(' '.join(map(str, i)))