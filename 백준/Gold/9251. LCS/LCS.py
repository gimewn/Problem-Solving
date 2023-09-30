one = input()
two = input()

DP = [[0]*(len(two)+1) for _ in range(len(one)+1)]

answer = 0

for i in range(len(one)):
    for j in range(len(two)):
        if one[i] == two[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        answer = max(answer, DP[i][j])

print(answer)