from collections import Counter
def solution(topping):
    answer = 0
    me = Counter(topping)
    brother = set()
    
    for top in topping:
        # 내 딕셔너리에서 해당 토핑 개수 1개 빼주기
        me[top] -= 1
        # 동생 set에 추가
        brother.add(top)
        
        # 만약 내 딕셔너리에서 0개가 된 토핑이 있다면 제거
        if me[top] == 0:
            me.pop(top)
        
        # 나와 동생의 토핑 개수가 같으면 answer ++
        if len(me) == len(brother):
            answer += 1
        
    return answer