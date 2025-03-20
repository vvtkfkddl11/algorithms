'''
1. 시간을 분으로 환산: 예) 15:10 15*60+10
2. 시작 순으로 sort
3. [i, i+1, i+2, ...] 에서 i, i+1 시간대가 겹치면 answer += 1
 - 겹치는 지는 어떻게 확인? 
    i의 끝나는 시각과 i+1의 시작 시각을 비교
    if i(끝나는 시각) + 10분 > i+1(시작 시각): answer += 1
'''

import heapq

def solution(book_time):
    answer = 0
    n = len(book_time)
    sorted_book_time = [[0] * 2 for _ in range(n)]
    
    for i in range(n):
        for j in range(2):
            hour, minute = map(int, book_time[i][j].split(":"))
            time = hour * 60 + minute
            sorted_book_time[i][j] = time
    
    print(sorted_book_time)
    sorted_book_time.sort(key=lambda x: x[0])
    print(sorted_book_time)
    
    lis = [] # queue
    for start, end in sorted_book_time:
        
        if lis and lis[0] + 10 <= start:
            heapq.heappop(lis)
        
        heapq.heappush(lis, end)
    answer = len(lis)
    
#     for i in range(n):
#         if sorted_book_time[i][1] + 10 > sorted_book_time[i+1][0]:
            
#             answer += 1
    
    return answer


