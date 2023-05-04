import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def dfs(now, lst, visit):
    if visit[now]:
        return
    visit[now] = 1
    for node in lst[now]:
        dfs(node, lst, visit)
    return


n, m = map(int, input().split())

dot = [[] for _ in range(n + 1)]
dot_reverse = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    dot[start].append(end)
    dot_reverse[end].append(start)

home, office = map(int, input().split())

answer = 0

# 집에서 갈 수 있는 (회사 도착 => 그만 탐색)
fromHome = [0] * (n + 1)
fromHome[office] = 1
dfs(home, dot, fromHome)

# 집까지 올 수 있는
toHome = [0] * (n + 1)
dfs(home, dot_reverse, toHome)

# 회사에서 갈 수 있는 (집 도착 => 그만 탐색)
fromOffice = [0] * (n + 1)
fromOffice[home] = 1
dfs(office, dot, fromOffice)

# 회사까지 올 수 있는
toOffice = [0] * (n + 1)
dfs(office, dot_reverse, toOffice)

for idx in range(1, n + 1):
    if idx == home or idx == office:
        continue
    if fromHome[idx] and toHome[idx] and fromOffice[idx] and toOffice[idx]:
        answer += 1

print(answer)