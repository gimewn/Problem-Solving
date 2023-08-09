import sys

def seperate_lecture(size):
    count = 0
    temp = 0
    for l in lectures:
        temp += l
        if temp > size:
            count += 1
            temp = l
    if temp:
        count += 1

    return count

N, M = map(int, sys.stdin.readline().split())

lectures = list(map(int, sys.stdin.readline().split()))

s = max(lectures)
e = 10**9

answer = 2e9

while s <= e:
    mid = (s + e) // 2
    if seperate_lecture(mid) <= M:
        answer = min(answer, mid)
        e = mid - 1
    else:
        s = mid + 1

print(answer)