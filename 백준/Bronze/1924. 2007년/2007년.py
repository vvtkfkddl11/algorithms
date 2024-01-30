def solution(x, y):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    sumYear = 0
    for i in range(x):
        sumYear += days[i]
    sumYear += y
    sumYear = sumYear % 7

    print(day[sumYear])


x, y = map(int, input().split())
solution(x, y)