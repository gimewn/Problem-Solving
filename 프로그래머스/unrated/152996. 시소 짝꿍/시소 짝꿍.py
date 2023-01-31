from collections import defaultdict

def solution(weights):
    answer = 0
    dict = defaultdict(int)

    for wei in weights:
        answer += dict[wei]+dict[wei*(2/3)]+dict[wei*(2/4)]+dict[wei*(3/2)]+dict[wei*(3/4)]+dict[wei*2]+dict[wei*(4/3)]
        dict[wei] += 1
        
    return answer