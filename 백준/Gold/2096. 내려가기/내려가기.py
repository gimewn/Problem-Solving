import sys

N = int(sys.stdin.readline())

DP = [[0]*3 for _ in range(2)] # 1행 = max, 2행 = min

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    for x in range(3): # 각 열마다 최댓값과 최솟값 찾아주기
        if x == 0:
            max_one = max(DP[0][0], DP[0][1])+a
            min_one = min(DP[1][0], DP[1][1])+a
        elif x == 1:
            max_two = max(DP[0][0], DP[0][1], DP[0][2])+b
            min_two = min(DP[1][0], DP[1][1], DP[1][2])+b
        else:
            max_three = max(DP[0][1], DP[0][2])+c
            min_three = min(DP[1][1], DP[1][2])+c

    DP = [[max_one, max_two, max_three], [min_one, min_two, min_three]] # 갱신

print(max(DP[0]), min(DP[1]))