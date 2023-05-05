import sys

input = sys.stdin.readline

T = int(input())

DP = [1]*10001

for idx in range(2, 10001):
    DP[idx] += DP[idx-2]

for idx in range(3, 10001):
    DP[idx] += DP[idx-3]

for _ in range(T):
    n = int(input())
    print(DP[n])