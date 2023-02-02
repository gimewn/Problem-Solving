def solution(s):
    answer = []
    zero = 0
    change = 0
    
    # 10진수 -> 2진수 변환 함수
    def change_two(num):
        res = ''
        while True:
            if num >= 2:
                res = str(num % 2) + res
                num //= 2
            else:
                res = str(num) + res
                return res
    
    while s != '1':
        # 0의 개수 세어서 더해주기
        zero += s.count('0')
        # 0 제거
        s = s.replace('0', '')
        length = len(s)
        # 길이를 2진수로 변환
        s = change_two(length)
        # 변환 횟수 더해주기
        change += 1
        
    return [change, zero]