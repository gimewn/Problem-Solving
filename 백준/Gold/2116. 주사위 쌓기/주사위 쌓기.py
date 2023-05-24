import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
dice = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mate = [5, 3, 4, 1, 2, 0]
side = [[1, 2, 3, 4], [0, 2, 4, 5], [0, 1, 3, 5], [0, 2, 4, 5], [0, 1, 3, 5], [1, 2, 3, 4]]
answer = -1

def DFS(level, top, total):
    global answer
    if level == n:
        answer = max(answer, total)
        return

    for i in range(6):
        if dice[level][i] == top:
            temp_max = 0
            for j in side[i]:
                temp_max = max(temp_max, dice[level][j])
            DFS(level+1, dice[level][mate[i]], total+temp_max)

for idx in range(6):
    DFS(0, dice[0][idx], 0)

print(answer)