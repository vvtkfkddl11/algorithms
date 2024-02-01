def solution(array, commands):
    answer = []
    newArr = []
    count = 0
    
    for i in (commands):
        newArr = array[i[0]-1:i[1]]
        newArr.sort()
        
        count = newArr[i[2]-1]
        
        answer.append(count)
        count = 0
        
    return answer