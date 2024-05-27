# ver2
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(numer1, denom1, numer2, denom2):
    # 1. 두 분수의 합 계산
    boonmo = denom1 * denom2
    boonja = numer1 * denom2 + numer2 * denom1
    
    # 2. 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer


    # temp = 0
    # if denom2 % denom1 == 0:
    #     if denom1 >= denom2:
    #         temp = denom1 / denom2
    #         answer.append((numer2*temp)+numer1)
    #         answer.append(denom1)
    #     else:
    #         temp = denom2 / denom1
    #         answer.append((numer1*temp)+numer2)
    #         answer.append(denom2)
    # else:
    #     answer.append((numer1*denom2)+(numer2*denom1))
    #     answer.append(denom1*denom2)