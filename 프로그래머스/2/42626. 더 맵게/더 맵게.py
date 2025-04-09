import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
        if scoville[0] == 0 and scoville[1] == 0:
            return -1
        
        # heapq.heapify(scoville)
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
        answer += 1
    
    if scoville[0] < K:
        return -1
            
    return answer