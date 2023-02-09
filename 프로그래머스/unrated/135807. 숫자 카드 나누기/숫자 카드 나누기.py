from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    # 배열의 최대 공약수 구하기
    def get_gcd(lst):
        res = lst[0]
        for idx in range(1, len(lst)):
            res = gcd(res, lst[idx])
        return res
    
    # 배열 A의 최대 공약수가 배열 B의 모든 원소를 나눌 수 없는지 혹은
    # 배열 B의 최대 공약수가 배열 A의 모든 원소를 나눌 수 없는지 확인
    def compare_gcd(lst, gcd_num):
        for num in lst:
            if num % gcd_num == 0:
                return 0
        return gcd_num
    
    # 각 배열의 최대 공약수
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)
    
    answer = max(answer, compare_gcd(arrayA, gcdB))
    answer = max(answer, compare_gcd(arrayB, gcdA))
            
    return answer