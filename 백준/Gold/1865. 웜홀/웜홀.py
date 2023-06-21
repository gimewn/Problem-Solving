import sys

def bellmanford(limit):
    check = [2e9]*limit
    check[0] = 0
    # 그래프 정점의 개수가 N개일 때, 시작 정점 => 특정 정점까지 거쳐가는 최대 간선은 N-1개
    # N-1 만큼 반복
    for i in range(N):
        for node in road:
            for value, cost in road[node]:
                # 더 적은 값으로 갱신
                if check[value] > cost + check[node]:
                    check[value] = cost + check[node]
                    # N번째에도 값이 갱신 => 음수 순환 존재
                    if i == N-1:
                        return True
    return False

TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    road = {}

    for idx in range(M+W):
        S, E, T = map(int, sys.stdin.readline().split())
        S, E = S-1, E-1

        if S not in road:
            road[S] = []
        if idx < M:
            road[S].append((E, T))
        else:
            road[S].append((E, -T))

        if idx < M:
            if E not in road:
                road[E] = []
            road[E].append((S, T))

    if bellmanford(N):
        print("YES")
    else:
        print("NO")