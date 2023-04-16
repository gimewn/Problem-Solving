def isCan(now, target):
    if now[1] > target[0]:
        return (now[0], min(now[1], target[1]))
    return False

def solution(targets):
    answer = 1
    targets.sort(key=lambda x : (x[0], x[1]))
    missile = [0, 1e9]
    
    for target in targets:
        res = isCan(missile, target)
        if not res:
            answer += 1
            missile = target
        else:
            missile = res

    return answer
