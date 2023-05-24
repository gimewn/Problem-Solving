n = int(input())
kids = [int(input()) for _ in range(n)]

dp = [1]*n

# LIS -> 정렬되어 있는 어린이 빼고 나머지를 옮기면 됨
for i in range(1, n):
    Max = 0
    for j in range(i):
        if kids[i] > kids[j]:
            Max = max(Max, dp[j])
    dp[i] += Max

print(n-max(dp))