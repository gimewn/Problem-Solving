def solution(n):
    answer = 0
    makethree = ''
    
    if n < 3:
        return n
    
    while True:
        makethree += str(n % 3)
        n //= 3
        if n < 3:
            makethree += str(n)
            break
    
    for idx in range(len(makethree)-1, -1, -1):
        answer += (3**idx)*int(makethree[len(makethree)-1-idx])
    
    return answer