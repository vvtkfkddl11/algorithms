s = input("")
newString = ""
arr = []
resultString = ""
flag = False

for i in range(len(s)):
    if s[i] == '<':
        if newString:
            arr.append(newString)
            newString = ""
        flag = True
        newString = newString + s[i]
    elif s[i] == '>':
        flag = False
        newString = newString + s[i]
        arr.append(newString)
        newString = ""
    elif flag:
        newString = newString + s[i]
    else:
        if s[i] == " ":  # + 마지막 인덱스일때
            arr.append(newString + " ")
            newString = ""
        else:
            newString = s[i] + newString

arr.append(newString)
resultString = "".join(arr)
print(resultString)