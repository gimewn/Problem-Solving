import sys

N, M = map(int, sys.stdin.readline().split())

people = [[] for _ in range(N)]
check = [0]*N
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    people[a].append(b)
    people[b].append(a)

def dfs(level, person):
    global answer

    if level == 4:
        print(1)
        exit(0)

    for friend in people[person]:
        if not check[friend]:
            check[friend] = 1
            dfs(level+1, friend)
            check[friend] = 0

for person in range(N):
    check[person] = 1
    dfs(0, person)
    check[person] = 0

print(0)