import sys

N, D, K, C = map(int, sys.stdin.readline().split())

sushi_belt = [int(sys.stdin.readline()) for _ in range(N)]

sushi_count = [0]*(D+1)

sushi_count[C] = 1

max_count = 0

start = 0

count = 1

for idx in range(K-1):
    sushi_count[sushi_belt[idx]] += 1
    if sushi_count[sushi_belt[idx]] == 1 and sushi_belt[idx] != C:
        count += 1

for end in range(K-1, N+K-1):
    end = end % N
    sushi_count[sushi_belt[end]] += 1

    if sushi_count[sushi_belt[end]] == 1:
        count += 1

    max_count = max(max_count, count)

    if sushi_count[sushi_belt[start]] == 1:
        count -= 1
    sushi_count[sushi_belt[start]] -= 1

    start += 1

print(max_count)