import sys

sys.setrecursionlimit(500000)

def dfs(now):
    global all_count

    for next_node in connect[now]:
        if not check[next_node] and next_node > 1:
            check[next_node] = check[now] + 1
            dfs(next_node)

N = int(sys.stdin.readline())

connect = [[] for _ in range(N+1)]

check = [0]*(N+1)

for _ in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split())

    connect[node1].append(node2)
    connect[node2].append(node1)

all_count = 0

dfs(1)

for node in range(1, N+1):
    if len(connect[node]) == 1:
        all_count += check[node]

if all_count % 2:
    print('Yes')
else:
    print('No')