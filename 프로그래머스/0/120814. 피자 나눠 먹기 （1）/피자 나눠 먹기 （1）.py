import math

def solution(n):
    answer = 0
    temp = float(n / 7)
    answer = math.ceil(temp)
    if answer < 1:
        answer = 1    
    return answer