import sys

sounds = sys.stdin.readline().strip()

# 각 상태별 카운터 (O(1) 접근)
q_count = 0      # "q" 상태
qu_count = 0     # "qu" 상태
qua_count = 0    # "qua" 상태
quac_count = 0   # "quac" 상태
max_ducks = 0    # 동시에 울었던 최대 오리 수

for char in sounds:
    if char == 'q':
        q_count += 1
        current_ducks = q_count + qu_count + qua_count + quac_count
        max_ducks = max(max_ducks, current_ducks)

    elif char == 'u':
        if q_count > 0:
            q_count -= 1
            qu_count += 1
        else:
            print(-1)
            exit()

    elif char == 'a':
        if qu_count > 0:
            qu_count -= 1
            qua_count += 1
        else:
            print(-1)
            exit()

    elif char == 'c':
        if qua_count > 0:
            qua_count -= 1
            quac_count += 1
        else:
            print(-1)
            exit()

    elif char == 'k':
        if quac_count > 0:
            quac_count -= 1
        else:
            print(-1)
            exit()
    else:
        print(-1)
        exit()

if q_count == 0 and qu_count == 0 and qua_count == 0 and quac_count == 0:
    print(max_ducks)
else:
    print(-1)