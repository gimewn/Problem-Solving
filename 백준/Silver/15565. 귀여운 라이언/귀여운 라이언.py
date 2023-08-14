import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
answer = 2e9
lion_location = []

for idx in range(N):
    if lst[idx] == 1:
        lion_location.append(idx)

length = len(lion_location)
if length < K:
    print(-1)
    exit(0)

s, e = 0, K-1

while e < length:
    answer = min(answer, lion_location[e] - lion_location[s])
    s += 1
    e += 1

print(answer + 1)