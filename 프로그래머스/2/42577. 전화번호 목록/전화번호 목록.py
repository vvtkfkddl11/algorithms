def solution(phone_book):
    answer = True
    dic = {}
    for i in phone_book: 
        dic[i] = 0
    for i in phone_book:
        prefix = ""
        for j in i:
            prefix += j
            if prefix in dic and i != prefix:
                return False
        
    return answer