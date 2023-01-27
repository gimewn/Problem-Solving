import itertools

def solution(numbers):
    answer = []
    comb = list(itertools.combinations(numbers, 2))

    for lst in comb:
        if sum(lst) not in answer:
            answer.append(sum(lst))
        
    answer.sort()
        
    return answer