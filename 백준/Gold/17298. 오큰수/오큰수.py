import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

max_ = [lst[-1]]

check = [-1]*n

for idx in range(n-2, -1, -1):
    # max_의 가장 마지막 값이 lst보다 작거나 같다면
    if max_[-1] <= lst[idx]:
        # max_의 마지막 값이 lst[idx]보다 클 때까지 pop
        while max_ and max_[-1] <= lst[idx]:
            max_.pop()
    # 만약 max_에 값이 있고, max_의 마지막 값이 lst[idx]보다 크면 기록
    if max_ and max_[-1] > lst[idx]:
        check[idx] = max_[-1]
    # lst[idx] 값 max_에 추가
    max_.append((lst[idx]))

print(*check)