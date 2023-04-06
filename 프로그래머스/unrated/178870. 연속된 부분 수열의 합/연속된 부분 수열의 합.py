def solution(sequence, k):
    answer = []
    end = 0
    sums = 0
    min_ans = 1e9
    
    for start in range(len(sequence)):
        while end < len(sequence) and sums < k:
            sums += sequence[end]
            end += 1
        if sums == k:
            if min_ans > end-start:
                answer = [start, end-1]
            min_ans = min(min_ans, end-start)
        sums -= sequence[start]
    
    return answer