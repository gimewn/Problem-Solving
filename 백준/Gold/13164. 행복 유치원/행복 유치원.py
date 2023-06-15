import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

kids = list(map(int, sys.stdin.readline().split()))

diff = []

answer = 0

for idx in range(1, N):
    diff.append(kids[idx] - kids[idx-1])

diff.sort(reverse=True)

for idx in range(K-1, N-1):
    answer += diff[idx]

print(answer)