def solution(s, n):
    answer = ''

    for i in s:
        if i == " ":
            answer += " "
            continue
        if 65 <= ord(i) <= 90:
            if ord(i)+n > 90:
                answer += chr((ord(i) - 65 + n) % 26 + 65)
            else: 
                answer += chr(ord(i)+n)
                print(i)
                print(ord(i))
        else:
            if ord(i)+n > 122:
                answer += chr((ord(i) - 97 + n) % 26 + 97)
            else:
                answer += chr(ord(i)+n)
        
    print(answer)
    
    return answer