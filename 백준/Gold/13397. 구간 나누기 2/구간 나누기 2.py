import sys

def divide_section(value):
    max_value = arr[0]
    min_value = arr[0]
    cnt = 1

    for idx in range(1, N):
        if max_value < arr[idx]:
            max_value = arr[idx]
        if min_value > arr[idx]:
            min_value = arr[idx]

        if max_value - min_value > value:
            cnt += 1
            max_value = arr[idx]
            min_value = arr[idx]

    return cnt

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

s, e = 0, max(arr) - 1

answer = e

while s <= e:
    mid = (s + e) // 2

    count = divide_section(mid)

    if count > M:
        s = mid + 1
    else:
        e = mid - 1
        answer = mid

print(answer)