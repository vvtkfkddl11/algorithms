import sys
import math
totalnum = int(sys.stdin.readline())
for i in range(totalnum):
    n, m = map(int, sys.stdin.readline().split())
    print(math.comb(m, n))