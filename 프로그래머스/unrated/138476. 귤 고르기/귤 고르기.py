from itertools import permutations, combinations

def solution(k, tangerine):
    answer = 0
    check = [0]*(max(tangerine)+1)
    
    # 종류별 개수 기록
    for t in tangerine:
        check[t] += 1
    
    # 개수 많은 순으로 역순 정렬
    check.sort(reverse=True)
    
    for checkT in check:
        # k에서 개수 많은 종류부터 빼보기
        k -= checkT
        # 종류 +1
        answer += 1
        # k가 0 이하라면 => 더 이상 상자에 안 담아도 됨
        if k <= 0:
            break
    
    return answer