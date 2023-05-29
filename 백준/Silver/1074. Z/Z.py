import sys, math

n, r, c = map(int, input().split())

visit = 0

def DFS(size, y, x):
    global visit
    if y == r and x == c:
        print(visit)
        exit(0)

    # (r, c)가 속하는 사분면이 아니라면
    if not y <= r < y + size and not x <= c < x + size:
        visit += size*size
        return

    if size == 1:
        visit += 1
        return

    DFS(size // 2, y, x)
    DFS(size // 2, y, x + size // 2)
    DFS(size // 2, y + size // 2, x)
    DFS(size // 2, y + size // 2, x + size // 2)

DFS(2**n, 0, 0)