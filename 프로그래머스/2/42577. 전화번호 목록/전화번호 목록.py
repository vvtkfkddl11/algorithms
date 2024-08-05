def solution(phone_book):
    answer = True
    hashMap = {}
    
    for i in phone_book:
        hashMap[i] = ''

    for number in phone_book:
        temp = ''
        for digit in number:
            temp += digit
            if temp in hashMap and temp != number:
                return False
    
    return True