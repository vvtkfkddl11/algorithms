def solution(arr):
    answer = []
    # 스택 or 큐 사용
    # i = 1
    # while i < len(arr):
    #     if arr[i] == arr[i-1]:
    #         arr.pop(i)
    #     else:
    #         answer.append(arr[i-1])
    #         i += 1
    # answer.append(arr[-1])
    answer = []
    for i in range(len(arr)):
        # 첫 번째 요소는 무조건 추가
        if i == 0:
            answer.append(arr[i])
        # 현재 요소가 이전 요소와 다를 때만 추가
        elif arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer
    return answer