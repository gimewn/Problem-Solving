def solution(X, Y):
    answer = ''
    exist = []
    numberX = [0]*10
    numberY = [0]*10
    
    for numX in X:
        numberX[int(numX)] += 1
    
    for numY in Y:
        numberY[int(numY)] += 1
    
    for num in range(9, -1, -1):
        temp = min(numberX[num], numberY[num])
        if temp > 0:
            answer += str(num)*temp
    
    if answer == '':
        return '-1'
    elif len(answer) == answer.count("0"):
        return '0'
    else:
        return answer