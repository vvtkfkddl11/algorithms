N = int(input())
count = 0

while N > 0:
    if N >= 3:
        N = N - 3
        count += 1
        # print(N, "3")
    elif N < 3:
        N = N - 1
        count += 1
        # print(N, "1")
    elif N == 0:
        break

if count % 2 == 1:
    print("SK")
else:
    print("CY")