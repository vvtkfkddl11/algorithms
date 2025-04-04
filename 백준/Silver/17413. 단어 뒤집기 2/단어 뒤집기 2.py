import sys

s = sys.stdin.readline().strip()

def solution(string):
    result = ""
    temp = ""
    is_tag = False
    
    for char in string:
        if char == '<':
            # 태그가 시작되기 전 누적된 단어를 뒤집어서 결과에 추가
            result += temp[::-1]
            temp = '<'
            is_tag = True
        elif char == '>':
            # 태그 닫기 문자를 포함하여 결과에 추가
            result += temp + '>'
            temp = ""
            is_tag = False
        elif char == ' ' and not is_tag:
            # 태그 밖의 공백인 경우, 앞에 누적된 단어를 뒤집어서 추가하고 공백도 추가
            result += temp[::-1] + ' '
            temp = ""
        else:
            # 문자 누적 (태그 내부 또는 단어)
            temp += char
    
    # 남은 문자열 처리
    if temp:
        result += temp[::-1]
    
    return result

print(solution(s))