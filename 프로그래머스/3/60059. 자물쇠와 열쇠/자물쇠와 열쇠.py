def rotate_key(key):
    M = len(key)
    return [[key[M - 1 - j][i] for j in range(M)] for i in range(M)]

def can_unlock(expanded_lock, key, x, y, N):
    M = len(key)
    # lock 복사본에 key를 적용
    for i in range(M):
        for j in range(M):
            expanded_lock[x + i][y + j] += key[i][j]

    # 자물쇠 영역이 모두 1로 채워졌는지 확인
    for i in range(N):
        for j in range(N):
            if expanded_lock[M - 1 + i][M - 1 + j] != 1:
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 확장된 자물쇠 만들기
    expanded_size = N + 2 * (M - 1)
    expanded_lock = [[0] * expanded_size for _ in range(expanded_size)]

    # 자물쇠 배치
    for i in range(N):
        for j in range(N):
            expanded_lock[M - 1 + i][M - 1 + j] = lock[i][j]

    # 키 회전과 이동
    for _ in range(4):
        key = rotate_key(key)
        for x in range(0, expanded_size - M + 1):
            for y in range(0, expanded_size - M + 1):
                if can_unlock([row[:] for row in expanded_lock], key, x, y, N):
                    return True

    return False