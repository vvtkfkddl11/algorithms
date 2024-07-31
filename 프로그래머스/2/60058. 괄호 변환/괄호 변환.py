def isBalance(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    if count == 0:
        return True
    return False

def isRight(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    return True

def makeRight(u, finalV):
    uLen = len(u)
    u = u[1:uLen-1]
    new_u = ''
    for i in u:
        if i == '(':
            i = ')'
        elif i == ')':
            i = '('
        new_u += i
        
    new_string = '(' + finalV + ')' + new_u
    return new_string

def solution(p):
    def dfs(s):
        temp = ''
        if s == '':
            return ''
        for i in range(len(s)): 
            temp += s[i]
            if isBalance(temp):
                u, v = temp, s[i+1:]
                if isRight(u):  # u가 올바른 괄호 문자열이 때
                    return u+dfs(v)
                else:  # u가 올바른 괄호 문자열이 아님
                    finalV = dfs(v)
                    return makeRight(u, finalV)
        return temp
    return dfs(p)
