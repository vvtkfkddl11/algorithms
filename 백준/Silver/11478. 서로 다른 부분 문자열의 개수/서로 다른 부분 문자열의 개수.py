string = input("")
result = set()

for i in range(len(string)):
    for j in range(i, len(string)):
        set.add(result, string[i:j+1])

print(len(result))
