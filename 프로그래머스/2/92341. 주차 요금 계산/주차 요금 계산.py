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

# from math import ceil # 올림


# def solution(fees, records):
#     answer = []
#     default_time, default_cost, unit_time, unit_cost = fees
#     start_time = 0
#     end_time = 0
#     car_in = {}
#     using_time = {}  # 번호: 누적 시간
    
#     for i in records:
#         time, number, io = i.split()
#         hour, minute = map(int, time.split(":"))
#         temp_time = hour * 60 + minute
        
#         if io == "IN":
#             car_in[number] = temp_time
            
#         else:
#             if number in using_time:
#                 using_time[number] += (temp_time - car_in[number])
#             else:
#                 using_time[number] = (temp_time - car_in[number])
    
#     # 하루 종료 시각까지 출차되지 않은 차량 처리
#     for number, time in car_in.items():
#         if number in using_time:
#             using_time[number] += 1439 - time
#         else:
#             using_time[number] = 1439 - time
    
#     # 차량번호 순으로 요금 계산
#     for number, time in sorted(using_time.items(), key = lambda x: x[0]):
#         fee = default_cost + max(0, ceil((time-default_time)/unit_time)) * unit_cost
#         answer.append(fee)
        
# #     # 'IN'(들어온 순서)을 기준으로 using_time 계산
# #     for number, time in car_in.items():  
# #         if number in using_time:  # 출차 기록이 있다면
# #             using_time[number] = using_time[number] - time
# #         else:  # 출차 기록이 없다면
# #             using_time[number] = 1439 - time # 23:59 -> 24시간*60분 - 1분
    

# #     for number, time in sorted(using_time.items(), key = lambda x : x[0]):
# #     fee = default_time - max(0, ceil((time-default_time)/unit_time)) * unit_fee
# #     answer.append(fee)
        
#     return answer