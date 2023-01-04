def solution(s):
    answer = []
    location = {}
    
    for idx in range(len(s)):
        if s[idx] in location.keys():
            answer.append(idx-location[s[idx]][-1])
            location[s[idx]].append(idx)
        else:
            location[s[idx]] = [idx]
            answer.append(-1)

    return answer