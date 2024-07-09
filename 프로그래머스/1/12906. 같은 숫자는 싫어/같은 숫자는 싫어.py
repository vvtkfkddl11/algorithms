def solution(arr):
    answer = []
    # 스택 or 큐 사용
    i = 1
    while i < len(arr):
        if arr[i] == arr[i-1]:
            arr.pop(i)
        else:
            i += 1
        
    answer = arr
    return answer