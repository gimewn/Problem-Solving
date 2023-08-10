import sys

N = int(sys.stdin.readline())

kids = [int(sys.stdin.readline()) for _ in range(N)]

DP = [1]*N

max_DP = 1

for first in range(1, N):
    max_value = 0
    for second in range(first):
        if kids[first] > kids[second]:
            max_value = max(max_value, DP[second])
    DP[first] += max_value
    max_DP = max(max_DP, DP[first])

print(N-max_DP)