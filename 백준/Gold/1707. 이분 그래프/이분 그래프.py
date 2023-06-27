import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append((0, start))
    check[start] = 1

    while q:
        parents, now = q.popleft()

        for child in connection[now]:
            if child == parents:
                continue
            if check[child] and check[child] == check[now]:
                return 0
            elif not check[child]:
                check[child] = check[parents]
                q.append((now, child))

    return 1

inputs = sys.stdin.readline
K = int(inputs())

for _ in range(K):
    V, E = map(int, inputs().split())
    check = [0]*(V+1)
    connection = [[] for _ in range(V+1)]
    answer = "YES"
    check[0] = 2

    for _ in range(E):
        u, v = map(int, inputs().split())
        connection[u].append(v)
        connection[v].append(u)

    for idx in range(1, V+1):
        if not check[idx]:
            res = bfs(idx)
            if not res:
                answer = "NO"
                break
    print(answer)