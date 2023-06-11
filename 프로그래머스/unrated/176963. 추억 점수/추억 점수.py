def solution(name, yearning, photo):
    miss = {}
    case = len(photo)
    answer = [0]*case
    
    for idx in range(len(name)):
        miss[name[idx]] = yearning[idx]
    
    for idx in range(case):
        for n in photo[idx]:
            if n in miss:
                answer[idx] += miss[n]
    
    return answer