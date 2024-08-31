# from itertools import combinations
# def solution(cards):
#     answer = 0
#     graph = [[] for i in range(len(cards))]
#     com = list(map(list, combinations(cards, 2)))
#     print(com)
    
#     for i in range(len(cards)):  # enumerate
#         graph[i].append(cards[i])
        
#     def dfs(node):
#         return 0
    
#     for i in com:
#         visited = [0]*len(cards)
#         dfs(i)
        
#     for i in graph:
#         visited = [0]*len(cards)
        
#         dfs(i)
    
    
#     print(graph)
#     return answer


from itertools import combinations

def dfs(cards, visited, start):
    group_size = 0
    current = start
    
    while not visited[current]:
        visited[current] = True
        next_box = cards[current] - 1  # 카드 번호가 다음 상자의 인덱스를 나타냅니다
        current = next_box
        group_size += 1
    
    return group_size

def solution(cards):
    n = len(cards)
    visited = [False] * n
    group_sizes = []
    
    # 모든 상자를 탐색하면서 그룹 크기를 구합니다.
    for i in range(n):
        if not visited[i]:
            group_size = dfs(cards, visited, i)
            group_sizes.append(group_size)
    
    # 최대 점수 계산 (두 개의 그룹 크기를 곱함)
    max_score = 0
    if len(group_sizes) > 1:
        for group1, group2 in combinations(group_sizes, 2):
            max_score = max(max_score, group1 * group2)
    
    return max_score