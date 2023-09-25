N = int(input())

schedule = [tuple(map(int, input().split())) for _ in range(N)]

DP = [0]*(N+1)

for idx in range(N-1, -1, -1):
    if schedule[idx][0] + idx > N:
        DP[idx] = DP[idx+1]
        continue
    prev = DP[idx+1]
    now = DP[schedule[idx][0]+idx] + schedule[idx][1]
    DP[idx] = max(DP[idx+1], DP[schedule[idx][0]+idx] + schedule[idx][1])

print(DP[0])