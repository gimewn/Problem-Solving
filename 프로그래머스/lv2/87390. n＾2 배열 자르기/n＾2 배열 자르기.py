def solution(n, left, right):
    answer = []
    for num in range(left, right+1):
        ty = num // n
        tx = num % n
        answer.append(max(ty+1, tx+1))
    
    return answer