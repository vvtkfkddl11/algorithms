def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10
        
        if digit < 5:
            # 내림: 현재 자릿수만큼 빼기
            answer += digit
            storey //= 10
        elif digit > 5:
            # 올림: 다음 자릿수로 올림
            answer += (10 - digit)
            storey = storey // 10 + 1
        else:  # digit == 5
            # 5인 경우 다음 자릿수 확인
            if (storey // 10) % 10 >= 5:
                # 올림
                answer += 5
                storey = storey // 10 + 1
            else:
                # 내림
                answer += 5
                storey //= 10
    
    return answer
