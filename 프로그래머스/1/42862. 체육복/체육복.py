def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
	
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)


# def solution(n, lost, reserve):
#     answer = 0

#     answer = n-len(lost)
#     for i in range(len(reserve)):
#         if reserve[i] not in lost:
#             # lost.remove(reserve[i])
#             answer += 1
#             if reserve[i]-1 in lost:
#                 print(i)
#                 answer += 1
#                 lost.remove(reserve[i]-1)
#                 print(lost)
#             elif reserve[i]+1 in lost:
#                 print(i)
#                 answer += 1
#                 lost.remove(reserve[i]+1)
#                 print(lost)
#             else:
#                 continue
#         else:
#             lost.remove(reserve[i])
#             answer += 1
        
#     return answer