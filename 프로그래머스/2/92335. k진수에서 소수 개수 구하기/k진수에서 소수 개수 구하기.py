def isK(n, k):
    result = ''
    while n: # 1)
        result += str(n % k) # 2) n으로 나눈 나머지를 answer에 추가
        n //= k # 3)
    return result[::-1] # 4) n진법 수

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = -1
    count = 0
    num = isK(n, k)
    nums = str(num).split("0")
    for i in nums:
    	# 1. i가 존재하고 2. 소수일 때
        if i and isPrime(int(i)):
            count += 1
    answer = count
    return answer