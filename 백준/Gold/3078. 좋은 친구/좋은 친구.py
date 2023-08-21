import sys

N, K = map(int, sys.stdin.readline().split())

friends = [len(sys.stdin.readline().rstrip()) for _ in range(N)]

check = [0]*21

start = 0

answer = 0

for idx in range(N):
    check[friends[idx]] += 1
    if check[friends[idx]] > 1:
        answer += check[friends[idx]] - 1
    if idx >= K:
        check[friends[start]] -= 1
        start += 1

print(answer)