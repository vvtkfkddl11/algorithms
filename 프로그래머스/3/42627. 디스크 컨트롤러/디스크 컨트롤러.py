import heapq


def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x:x[0])
    print(jobs)
    waiting = []
    total_time = 0
    current_time = 0
    completed = 0
    i = 0
    
    while completed <= len(jobs):
        while i < len(jobs) and current_time <= jobs[i][0]:
            heapq.heappush(waiting, (jobs[i][1], jobs[i][0], i))
            i += 1
        if waiting:
            duration, request_time, job_idx = heapq.heappop(waiting)
            current_time += duration
            total_time = current_time - request_time
            completed += 1
        else:
            if i < len(jobs):
                current_time = jobs[i][0]
            
    
    return total_time // len(jobs)