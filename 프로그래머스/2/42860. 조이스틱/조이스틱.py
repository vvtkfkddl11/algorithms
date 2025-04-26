def solution(name):
    cnt = 0
    pos_A = ord('A')  # 초기 위치 A 아스키 변환: 65
    pos_Z = ord('Z')
    
    # 커서 이동에 필요한 최소 조작 횟수 계산
    length = len(name)
    move = length - 1  # 기본적으로 오른쪽으로 쭉 이동하는 경우
    
    for i in name:
        # 초기 위치에서 바로 이동, Z로 갔다가 이동 횟수 비교
        cnt += min(ord(i) - pos_A, 1 + pos_Z - ord(i))
    
    # 왼쪽에서 오른쪽으로, 오른쪽에서 왼쪽으로 방향 전환하는 모든 경우 고려
    for i in range(length):
        next_i = i + 1
        # 현재 위치 다음부터 연속된 A의 끝부분 찾기
        while next_i < length and name[next_i] == 'A':
            next_i += 1
            
        # 방법 1: i까지 오른쪽으로 갔다가 다시 왼쪽으로 돌아가는 경우
        # 방법 2: 처음부터 왼쪽으로 가는 경우 (양 끝점 간 이동)
        move = min(move, i + i + length - next_i)  # 2*i + length - next_i
        
        # 방법 3: 처음부터 왼쪽으로 갔다가 다시 오른쪽으로 돌아가는 경우
        move = min(move, (length - next_i) * 2 + i)
    
    # 전체가 A인 경우 예외 처리
    if move < 0:
        move = 0

    return cnt + move