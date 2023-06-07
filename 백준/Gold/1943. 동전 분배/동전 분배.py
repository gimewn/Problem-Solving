import sys

for _ in range(3):

    N = int(input())
    total_coin = 0
    answer = 0
    half = 0
    coins = {}

    for _ in range(N):
        kind_of, cnt = map(int, sys.stdin.readline().split())
        total_coin += kind_of*cnt
        coins[kind_of] = cnt

    if total_coin % 2 == 0:
        half = total_coin // 2
        DP = [0] * (half+1)
        DP[0] = 1

        for c in coins:
            value, value_cnt = c, coins[c]
            for cost in range(half, -1, -1):
                if DP[cost]:
                    for cnt in range(1, value_cnt + 1):
                        if cost + value * cnt <= half:
                            DP[cost + value*cnt] += 1

        if DP[-1]:
            print(1)
        else:
            print(0)

    else:
        print(0)