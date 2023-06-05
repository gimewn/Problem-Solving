def LCS(word1, word2):
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1] == word2[j-1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

one = input()
two = input()

DP = [[0]*(len(two)+1) for _ in range(len(one)+1)]

LCS(one, two)

print(DP[-1][-1])