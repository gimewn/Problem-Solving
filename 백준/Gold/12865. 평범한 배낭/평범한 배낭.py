N, K = map(int, input().split())
md = [list(map(int, input().split())) for _ in range(N)]
md.sort(key=lambda x:x[0])

bag = [[0]*(K+1) for _ in range(N+1)]

for y in range(1, N+1):
    for x in range(1, K+1):
        if md[y-1][0] > x:
            bag[y][x] = bag[y-1][x]
        else:
            bag[y][x] = max(md[y-1][1]+bag[y-1][x-md[y-1][0]], bag[y-1][x])
print(bag[N][K])