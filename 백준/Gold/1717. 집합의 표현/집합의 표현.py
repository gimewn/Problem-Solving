import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    parents[b] = a
        
for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")