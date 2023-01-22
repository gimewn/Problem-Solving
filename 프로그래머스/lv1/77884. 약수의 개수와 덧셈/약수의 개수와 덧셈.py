def cal(number):
    res = 0
    for num in range(1, number+1):
        if number % num == 0:
            res += 1
    return res

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if cal(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer