import sys

N, D, K, C = map(int, sys.stdin.readline().split())

sushi_belt = [int(sys.stdin.readline()) for _ in range(N)]

sushi_count = {}

max_count = 0

start = 0

for idx in range(K-1):
    if sushi_belt[idx] not in sushi_count:
        sushi_count[sushi_belt[idx]] = 0
    sushi_count[sushi_belt[idx]] += 1

for end in range(K-1, N+K-1):
    end = end % N
    if sushi_belt[end] not in sushi_count:
        sushi_count[sushi_belt[end]] = 0
    sushi_count[sushi_belt[end]] += 1

    this_count = len(sushi_count.keys())

    if C not in sushi_count:
        this_count += 1

    max_count = max(max_count, this_count)

    sushi_count[sushi_belt[start]] -= 1

    if not sushi_count[sushi_belt[start]]:
        del sushi_count[sushi_belt[start]]

    start += 1

print(max_count)