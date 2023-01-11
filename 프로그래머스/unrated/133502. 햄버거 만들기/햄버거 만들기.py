def solution(ingredient):
    answer = 0
    hambuger = []
    
    for ing in ingredient:
        hambuger.append(ing)
        if hambuger[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                hambuger.pop()
        
    return answer