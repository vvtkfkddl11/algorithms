from math import ceil # 올림

def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees
    
    # 현재 주차장에 있는 차량의 입차 시간을 저장하는 딕셔너리
    parking = {}
    
    # 각 차량의 누적 주차 시간을 저장하는 딕셔너리
    using_time = {}
    
    for record in records:
        time, number, io = record.split()
        hour, minute = map(int, time.split(":"))
        time = hour*60 + minute
        
        # 입차 시
        if io == "IN":
            parking[number] = time # 주차장에 차량 입차 시간을 기록
            
        # 출차 시
        elif io == "OUT":
            
            # 차량번호가 using_time 딕셔너리에 존재하면
            if number in using_time:
                using_time[number] += (time - parking[number]) # 누적
            
            # 아니면
            else:
                using_time[number] = time - parking[number] # 할당
            
            # 출차 후 주차장에서 차량 제거
            del parking[number]
        
    # 하루 종료 시각까지 출차되지 않은 차량 처리
    for number, time in parking.items():
        if number in using_time:
            using_time[number] += 1439 - time
        else:
            using_time[number] = 1439 - time
            
    # 차량번호 순으로 요금 계산
    for number, time in sorted(using_time.items(), key = lambda x: x[0]):
        fee = default_fee + max(0, ceil((time-default_time)/unit_time)) * unit_fee
        answer.append(fee)
            
    return answer