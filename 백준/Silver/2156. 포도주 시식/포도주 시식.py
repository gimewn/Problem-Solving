N = int(input())

alcohol = [0]+[int(input()) for _ in range(N)]

DP = [0]*(N+1)

DP[1] = alcohol[1]

for idx in range(2, N+1):
    DP[idx] = alcohol[idx]+max(DP[idx-2], DP[idx-3]+alcohol[idx-1])
    DP[idx] = max(DP[idx-1], DP[idx])

print(DP[-1])