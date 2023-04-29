import sys

input = sys.stdin.readline

N = int(input())
# A -> B, B -> A
move = (0, 0)
DP = [[0, 0] for _ in range(N)]

for idx in range(N):
    temp = list(map(int, input().split(" ")))
    # A라인
    DP[idx][0] = min(DP[idx-1][0], DP[idx-1][1] + move[1]) + temp[0]
    # B라인
    DP[idx][1] = min(DP[idx-1][1], DP[idx-1][0] + move[0]) + temp[1]

    if idx < N-1:
        move = (temp[2], temp[3])

print(min(DP[N-1]))