import sys

# 1 => 0
# 2 => 3 = 3
# 3 => 0
# 4 => dp[2] * dp[2] + 2 = 11
# 5 => 0
# 6 => dp[4] * dp[2] + dp[2] * 2 + 2 = 41
# 7 => 0
# 8 => dp[6] * dp[2] + dp[4] * 2 + dp[2] * 2 + 2 = 153
# 점화식 : dp[n] = dp[n - 2] * dp[2] + dp[n - 4] * 2 ... + 2

n = int(sys.stdin.readline())
dp = [0] * 31
dp[2] = 3

# 반복문을 통해 점화식을 수행
for i in range(4, n + 1):

    # 짝수만을 타일로 채울 수 있다.
    if i % 2 == 0:
        dp[i] += dp[i - 2] * dp[2]

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2 # dp[j]에 특수한 모양 2개의 조합

        dp[i] += 2 # 특수한 모양 2개 추가

print(dp[n])