import sys

N = int(input())
lst = []

for _ in range(N):
    y, x = map(int, sys.stdin.readline().split())
    lst.append((y, x))

DP = [[2e9]*N for _ in range(N)]

for i in range(N):
    DP[i][i] = 0

# i => 곱할 행렬 개수 -1
# i == 1 => 2개의 행렬 곱함
for i in range(1, N):
    # i+1개의 행렬 곱할 수 있는 수
    # N이 4고 i가 3 => 4개의 행렬을 곱할 수 있는 위치 => 0
    for j in range(N-i):
        # 곱할 행렬이 2개이면 서로 곱해서 기록해주기
        if i == 1:
            DP[j][j+1] = lst[j][0]*lst[j][1]*lst[j+1][1]
            continue

        # j부터 j+i의 중간 과정
        # (j, k)(k+1, j+i)
        for k in range(j, j+i):
            DP[j][j+i] = min(DP[j][j+i], DP[j][k] + DP[k+1][j+i] + lst[j][0]*lst[k][1]*lst[j+i][1])

print(DP[0][-1])