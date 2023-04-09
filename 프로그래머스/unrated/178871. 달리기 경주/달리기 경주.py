def solution(players, callings):
    
    seq = {}
    player = {}
    
    for idx in range(len(players)):
        seq[idx+1] = players[idx]
        player[players[idx]] = idx+1
    
    for c in callings:
        # 언급된 선수 등수 1 줄여주기
        player[c] -= 1
        # 언급된 선수의 갱신 등수
        now = player[c]
        # 갱신 등수에 원래 있던 선수
        prev = seq[now]
        # 갱신 등수 => 언급된 선수로 교체
        seq[now] = c
        # 원래 등수 => 갱신 등수에 있던 선수로 교체
        seq[now+1] = prev
        # 갱신 등수에 있던 선수 등수 1 늘려주기
        player[prev] += 1
        
    return list(seq.values())