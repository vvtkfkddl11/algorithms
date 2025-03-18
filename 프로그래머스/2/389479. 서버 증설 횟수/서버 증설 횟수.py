
# def solution(players, m, k):
#     answer = 0
#     servers_made = [0]*24

#     for i in range(len(players)):
#         if players[i]//m >= servers_made[i]: # >= 로 해도 됨
#             needed_servers = (players[i]//m) - servers_made[i]
#             answer += needed_servers
#             for j in range(i, min(i + k, 24)):
#                 servers_made[j] += needed_servers
    
#     return answer

def solution(players, m, k):
    answer = 0
    servers_made = [0]*24

    for i in range(len(players)):
        if (players[i]//m) - servers_made[i] < 0:  # if문 필요없음
            needed_servers = 0
        else:
            needed_servers = (players[i]//m) - servers_made[i]
            answer += needed_servers
        
            for j in range(i, min(i + k, 24)):
                # if needed_servers >= servers_made[j]:  # 이거 때문에 오답
                    servers_made[j] += needed_servers    
    return answer
