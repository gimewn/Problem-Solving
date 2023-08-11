import sys

def find_shoot(x, y):
    global answer

    s, e = 0, M-1

    start = x + y - L
    end = x - y + L

    while s <= e:
        mid = (s + e) // 2
        if start <= shoot[mid] <= end:
            answer += 1
            return
        elif start > shoot[mid]:
            s = mid + 1
        elif end < shoot[mid]:
            e = mid - 1

M, N, L = map(int, sys.stdin.readline().split())

shoot = list(map(int, sys.stdin.readline().split()))

animal = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

shoot.sort()

answer = 0

for x, y in animal:
    if y > L:
        continue
    find_shoot(x, y)

print(answer)
