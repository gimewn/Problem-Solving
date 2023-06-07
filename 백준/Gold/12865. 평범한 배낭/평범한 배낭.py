import sys

def check_value():
    for i in range(N):
        for j in range(K + 1):
            if j < items[i][0]:
                bags[i][j] = bags[i - 1][j]
            else:
                # bags[i-1][j-items[i][0]]
                # bags[i][j-items[i][0]]일 경우, 자기 자신을 2번 더할 수 있음
                # 6 => 3 3
                # items를 정렬해주고, bags[i-1]을 참조함
                bags[i][j] = max(bags[i - 1][j], bags[i - 1][j - items[i][0]] + items[i][1])

N, K = map(int, sys.stdin.readline().split())

bags = [[0]*(K+1) for _ in range(N)]

items = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    items.append((W, V))

items.sort()

check_value()

print(bags[-1][-1])