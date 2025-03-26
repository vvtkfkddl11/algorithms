def solution(nums):
    answer = 0
    n_choice = len(nums)//2
    if n_choice < len(set(nums)):
        return n_choice
    answer = len(set(nums))
    return answer



# def solution(nums):
#     answer = 0
#     n_choice = len(nums)//2
#     dic = {}
#     dic2 = {}
#     for i in nums:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
    
#     if len(dic.keys()) >= n_choice:
#         return n_choice
    
#     temp = 0
#     while sum(dic2.values()) < n_choice:
#         for key, value in dic.items():
#             if value > 0:
#                 value -= 1
#                 temp += 1
#                 if value not in dic2:
#                     dic2[key] = 1
#                 else:
#                     dic2[key] += 1
#     # print(dic2)
#     answer = len(dic2)
#     return answer







# from itertools import combinations

# def solution(nums):
#     answer = 0
#     n_choice = len(nums)//2
#     max_kinds = 0
#     arr = list(combinations(nums, n_choice))
#     nums_list = []
#     for i in arr:
#         nums_list.append(list(i))
#     for i in nums_list:
#         max_kinds = max(max_kinds, len(set(i)))
#     return max_kinds