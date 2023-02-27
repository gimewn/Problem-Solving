N = int(input())

dp = [0]*31

dp[2] = 3

for idx in range(4, N+1):
    if idx % 2 == 0:
        # dp[idx-2]의 경우의 수 * dp[2]의 경우의 수
        dp[idx] += dp[idx-2]*dp[2]

        # 4 이상일 경우, 나올 수 있는 특이한 모양 2개 존재
        for i in range(idx-4, -1, -2):
            dp[idx] += dp[i] * 2

        # idx에서만 나올 수 있는 특이한 모양 2개
        dp[idx] += 2

print(dp[N])