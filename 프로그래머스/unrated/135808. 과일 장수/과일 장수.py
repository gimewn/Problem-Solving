def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for idx in range(0, len(score), m):
        temp = score[idx:idx+m]
        if len(temp) == m:
            answer += min(temp)*m

    return answer