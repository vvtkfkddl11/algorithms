from collections import Counter

s = input("")
s = s.upper()
countString = Counter(s).most_common()

if len(s) == 1 or len(countString) == 1:
    print(countString[0][0])
elif countString[0][1] == countString[1][1]:
    print("?")
else:
    print(countString[0][0])