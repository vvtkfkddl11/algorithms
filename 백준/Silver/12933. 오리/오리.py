import sys

sounds = str(sys.stdin.readline().strip())
arr = []
flag = 0
answer = 0

for i in sounds:
    if i == 'q':
        if 'quack' in arr:
            for j in range(len(arr)):
                if arr[j] == 'quack':
                    arr[j] = 'q'
                    break
        else:
            arr.append(i)
    elif i == 'u':
        if 'q' in arr:
            for j in range(len(arr)):
                if arr[j] == 'q':
                    arr[j] += 'u'
                    break
        else:
            flag = 1
            break
    elif i == 'a':
        if 'qu' in arr:
            for j in range(len(arr)):
                if arr[j] == 'qu':
                    arr[j] += 'a'
                    break
        else:
            flag = 1
            break
    elif i == 'c':
        if 'qua' in arr:
            for j in range(len(arr)):
                if arr[j] == 'qua':
                    arr[j] += 'c'
                    break
        else:
            flag = 1
            break
    elif i == 'k':
        if 'quac' in arr:
            for j in range(len(arr)):
                if arr[j] == 'quac':
                    arr[j] += 'k'
                    break
        else:
            flag = 1
            break
    else:
        flag = 1
        break

if flag == 1:
    print(-1)
else:
    for i in arr:
        if i != 'quack':
            print(-1)
            exit(0)
        else:
            answer += 1
    if answer == 0:
        print(-1)
    else:
        print(answer)