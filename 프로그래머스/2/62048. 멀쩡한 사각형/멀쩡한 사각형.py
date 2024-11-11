import math

def solution(w,h):
    answer = 1
    temp = math.gcd(w, h)
    answer = (w*h)-(w+h-temp)
    return answer

'''
공식 따로 있음
사용할 수 없는 정사각형의 개수 = w + h - w와 h의 최대공약수
https://ranseo.tistory.com/210
'''