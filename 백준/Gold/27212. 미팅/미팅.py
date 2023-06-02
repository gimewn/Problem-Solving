import sys

N, M, C = map(int, sys.stdin.readline().split())

satisfaction = [[0]*(C+1)] + [[0]+ list(map(int, sys.stdin.readline().split())) for _ in range(C)]

A = [0] + list(map(int, sys.stdin.readline().split()))
B = [0] + list(map(int, sys.stdin.readline().split()))

DP = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = max(DP[i-1][j], DP[i][j-1], DP[i-1][j-1] + satisfaction[A[i]][B[j]])

print(DP[-1][-1])