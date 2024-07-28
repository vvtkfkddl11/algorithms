def solution(enroll, referral, seller, amount):
    answer = []
    graph = {}
    income = {i: 0 for i in enroll}  # 이름: 수익

    # 자식: 부모
    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]

    def distribution(child, amount):
        if child == '-' or amount < 1:  # 1원 이하면 자식이 가져감?
            return
        parent = graph[child]
        pay = int(amount * 0.1)  # amount // 10
        income[child] += (amount - pay)
        distribution(parent, pay)

    for i, child in enumerate(seller):
        initial_amount = amount[i] * 100
        distribution(child, initial_amount)
    
    answer = [income[name] for name in enroll]
    return answer
    

# def solution(enroll, referral, seller, amount):
#     answer = []
#     names_dic = {name: 0 for name in enroll}
#     graph = {name: [] for name in enroll}
    
#     # # 그래프를 만듦
#     # for i in range(len(enroll)):
#     #     if referral[i] != "-":
#     #         graph[enroll[i]].append(referral[i])
#     #         graph[referral[i]].append(enroll[i])
    
#     for i in range(len(enroll)):
#         if referral[i] != "-":
#             graph[enroll[i]].append(referral[i])
#             graph[referral[i]].append(enroll[i])
#     for i in range(len(seller)):
#         print(seller[i])
#         if amount[i] * 
        
#     print(names_dic)
#     print(graph)
    
#     # ten_percent = amount * 0.1
    
#     # for i in enroll:
#     #     names_dic[i] = 0
                     
#     # for parent in enroll:
#     #     for child in referral:
#     #         graph[parent] += [child]
#     #         graph[child] += [parent]
                    
#     return answer