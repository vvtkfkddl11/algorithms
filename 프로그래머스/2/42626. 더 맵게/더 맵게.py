import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)
    new_scoville = 0
    while len(scoville) >= 2 and scoville[0] < K: 
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new_scoville = (a + b*2)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer