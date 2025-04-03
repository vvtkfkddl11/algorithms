import sys

s = str(sys.stdin.readline().strip())

def solution(strs):
    answer = ""
    arr = []
    flag = 0
    reverse_strs = ""
    tag_strs = ""

    for i in range(len(strs)):
        if strs[i] == ">":
            tag_strs += strs[i]
            arr.append(tag_strs)
            tag_strs = ""
            flag = 0
        elif strs[i] == "<" or flag == 1:
            if reverse_strs:
                arr.append(reverse_strs)
                reverse_strs = ""
            flag = 1
            tag_strs += strs[i]
        elif strs[i] == " ":
            reverse_strs += " "
            arr.append(reverse_strs)
            reverse_strs = ""
        elif i == (len(strs)-1):
            reverse_strs = (strs[i] + reverse_strs)
            arr.append(reverse_strs)
        else:
            reverse_strs = (strs[i] + reverse_strs)

    for i in arr:
        answer += i
    return answer


print(solution(s))