def solution(n, lost, reserve):
    answer = 0
    # 여벌 체육복을 가져왔지만 도난당한 학생 처리
    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))
    
    for i in list(set_lost):
        print(i)
        if i-1 in set_reserve:
            set_lost.remove(i)
            set_reserve.remove(i-1)
            print(set_lost)
        elif i+1 in set_reserve:
            set_lost.remove(i)
            set_reserve.remove(i+1)
            print(set_lost)
    answer = (n - len(set_lost))
    return answer
