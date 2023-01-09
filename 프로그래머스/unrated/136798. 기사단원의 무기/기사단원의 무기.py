

def solution(number, limit, power):
    answer = 0
    
    # 약수 개수를 구해주는 함수
    def getDivisor(param):
        res = 0
        for num in range(1, int(param**(1/2))+1):
            if param % num == 0:
                res += 1
                # 제곱근이 param이 아니면 짝이 있다는 뜻
                if num**2 != param:
                    res += 1
            # 약수의 개수가 limit을 넘겼다면 power를 리턴하고 종료
            if res > limit:
                return power
        return res
    
    # 1~number까지 각 약수의 개수를 구해 제한수치를 넘는지 판단, answer에 더해주기
    for num in range(1, number+1):
        temp = getDivisor(num)
        if temp > limit:
            answer += power
        else:
            answer += temp
    
    return answer