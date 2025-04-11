def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    print(people)
    
    # left, right 자체가 인덱스 역할
    left = 0
    right = len(people) - 1
    
    while left <= right:
        # if left == right:
        #     answer += 1
        #     break
        if people[left] + people[right] <= limit:
            right -= 1
        left += 1
        answer += 1
    return answer