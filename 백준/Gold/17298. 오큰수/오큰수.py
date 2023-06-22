import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

max_ = [lst[-1]]

check = [-1]*n

for idx in range(n-2, -1, -1):
    if max_[-1] <= lst[idx]:
        while max_ and max_[-1] <= lst[idx]:
            max_.pop()
    if max_ and max_[-1] > lst[idx]:
        check[idx] = max_[-1]
    max_.append((lst[idx]))

print(*check)