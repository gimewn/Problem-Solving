def solution(word):
    answer = 0
    cnt = 0
    def DFS(level, now):
        nonlocal word, answer, cnt
        
        if now == word:
            answer = cnt
            return
        
        if level >= 5:
            return
        if answer == 0:
            for alp in ['A', 'E', 'I', 'O', 'U']:
                cnt += 1
                DFS(level+1, now+alp)
    DFS(0, '')

    return answer