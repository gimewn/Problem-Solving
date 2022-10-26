import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

s = 1
e = max(tree)

while s<=e:
    take = 0
    mid = (s+e)//2
    for i in tree:
        if i > mid:
            take += i-mid
    if take >= M:
        s = mid+1
    elif take < M:
        e = mid-1
print(e)