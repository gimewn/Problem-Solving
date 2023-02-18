def solution(cards):
    answer = 0
    length = len(cards)

    for first in range(length):
        visited01 = [0] * length
        pick = cards[first]
        
        while visited01[pick - 1] == 0:
            visited01[pick - 1] = 1
            pick = cards[pick - 1]
            
        for second in range(first + 1, length):
            pick = cards[second]
            visited02 = visited01[:]
            
            while visited02[pick - 1] == 0:
                visited02[pick - 1] = 2
                pick = cards[pick - 1]
                
            score = visited01.count(1) * visited02.count(2)
            answer = max(answer, score)
            
    return answer