def solution(number):
    answer = 0
    def DFS(num, level, prev):
        nonlocal answer, number
        if level == 3:
            if num == 0:
                answer += 1
            return

        for idx in range(prev+1, len(number)):
            DFS(num+number[idx], level+1, idx)

    DFS(0, 0, -1)
    return answer