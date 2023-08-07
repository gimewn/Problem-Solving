import sys

N, C = map(int, sys.stdin.readline().split())

town = [int(sys.stdin.readline()) for _ in range(N)]
length = len(town)
answer = 0

town.sort()

start = 1
end = town[-1] - town[0]

while start <= end:
    mid = (start + end) // 2
    prev = town[0]
    count = 1

    for idx in range(1, length):
        if town[idx] >= prev+mid:
            count += 1
            prev = town[idx]

    if count >= C:
        start = mid + 1
        answer = mid
    elif count < C:
        end = mid - 1

print(answer)