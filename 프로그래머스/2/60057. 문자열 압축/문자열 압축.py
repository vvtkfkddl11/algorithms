def solution(s):
    result = []
    for i in range(1, len(s)+1):
        shortenString = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s)+i, i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    shortenString = shortenString + str(cnt) + temp
                else:
                    shortenString = shortenString+temp
                temp = s[j:j + i]
                cnt = 1
        result.append(len(shortenString))
    return min(result)