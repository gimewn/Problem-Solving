def solution(k, dungeons):
    answer = 0
    length = len(dungeons)

    def dfs(now, level, done):
        nonlocal answer

        if done > answer:
            answer = done

        for idx in range(length):
            if check[idx] == 0 and now >= dungeons[idx][0]:
                check[idx] = 1
                dfs(now - dungeons[idx][1], level + 1, done + 1)
                check[idx] = 0

    check = [0] * length

    dfs(k, 0, 0)

    return answer