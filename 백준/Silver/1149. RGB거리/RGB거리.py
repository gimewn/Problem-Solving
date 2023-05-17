n = int(input())
check = [-1]*n
answer = 2e9
home = [list(map(int, input().split())) for _ in range(n)]

# 빨초파 순서로 각 색마다 앞에 올 수 있는 색
# 빨(0) : 초(1) 파(2)
# 초 : 빨 파
# 파 : 빨 초
dir = [[1, 2], [-1, 1], [-2, -1]]

DP = [[0, 0, 0] for _ in range(n)]

DP[0] = home[0]

for h in range(1, n):
    for color in range(3):
        first, second = dir[color][0], dir[color][1]
        # 앞에 올 수 있는 색 중 값이 더 작은 것과 현재 색 더해주기
        DP[h][color] = min(DP[h-1][color+second], DP[h-1][color+first]) + home[h][color]

print(min(DP[-1]))