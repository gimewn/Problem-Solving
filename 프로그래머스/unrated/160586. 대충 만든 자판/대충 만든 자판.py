def solution(keymap, targets):
    answer = []
    alp = {}
    
    for key in keymap:
        for idx in range(len(key)):
            if key[idx] in alp:
                alp[key[idx]] = min(alp[key[idx]], idx+1)
            else:
                alp[key[idx]] = idx+1
    
    for target in targets:
        cnt = 0
        for word in target:
            if word in alp:
                cnt += alp[word]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer