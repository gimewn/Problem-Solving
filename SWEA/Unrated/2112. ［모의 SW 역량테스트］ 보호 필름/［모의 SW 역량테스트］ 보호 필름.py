from copy import deepcopy

T = int(input())

for t in range(1, T+1):
    def check_performance(board, k):
        for y in range(len(board[0])):
            count = 0
            prev = board[0][y]
            for x in range(1, len(board)):
                now = board[x][y]
                if prev == now:
                    count += 1
                else:
                    count = 0
                if count == k-1:
                    break
                prev = now
            if count < K-1:
                return False
        return True

    def dfs(level, idx):
        global answer
        if level >= answer:
            return

        if check_performance(board, K):
            answer = min(answer, level)
            return

        for i in range(idx+1, D):
            origin = deepcopy(board[i])
            for type in [0, 1]:
                board[i] = [type]*W
                dfs(level+1, i)
            board[i] = origin

    """
    D = 보호 필름 두께
    W = 가로 크기
    K = 합격 기준
    """
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    answer = D

    dfs(0, -1)

    print(f'#{t} {answer}')