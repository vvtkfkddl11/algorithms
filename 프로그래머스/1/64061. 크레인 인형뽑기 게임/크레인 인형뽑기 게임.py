def solution(board, moves):
    answer = 0
    stack = []  # 바구니
    for i in moves:
        for j in range(len(board)):
            # 현재 타켓 인형: board[j][i-1]
            if board[j][i-1] != 0:  # 타켓 인형이 0이 아닐 때                
                if not stack:
                    stack.append(board[j][i-1])
                    # board[j][i-1] = 0
                else:
                    if stack[-1] == board[j][i-1]:  # 바구니 맨 위의 인형과 같을 때
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[j][i-1])  # 바구니 맨 위의 인형과 다를 때
                        # board[j][i-1] = 0
                board[j][i-1] = 0
                break
            else:  # 타켓 인형이 0일 때
                continue
    
    return answer