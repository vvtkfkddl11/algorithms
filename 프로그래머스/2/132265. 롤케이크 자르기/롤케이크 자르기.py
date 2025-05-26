'''
구글링
아이디어
1. 미리 계산: 각 위치까지의 누적 토핑 종류 수를 전부 계산
2. 역방향 계산: 뒤에서부터도 누적 계산해서 대칭 구조 활용
'''
def solution(topping):
    answer = []
    right_num, left_num = [], []
    right_set, left_set = set(), set()
    for i in topping:
        right_set.add(i)
        right_num.append(len(right_set))
    for i in topping[::-1]:
        left_set.add(i)
        left_num.append(len(left_set))
    for i in range(len(right_num) - 1):  
        left_types = right_num[i]        # 왼쪽 토핑 종류 수
        right_types = left_num[len(left_num) - i - 2]  # 오른쪽 토핑 종류 수
        if left_types == right_types:    # 양쪽 종류 수가 같으면
            answer.append(i)             # 해당 자르는 위치를 저장
    # 자르는 방법의 '개수'만 반환
    return len(answer)