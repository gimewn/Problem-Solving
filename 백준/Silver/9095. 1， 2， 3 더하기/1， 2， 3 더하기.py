import sys

input = sys.stdin.readline

DP = [1]*12
DP[2] = 2

for idx in range(3, 12):
    DP[idx] = DP[idx-1] + DP[idx-2] + DP[idx-3]

T = int(input())

for _ in range(T):
    n = int(input())
    print(DP[n])