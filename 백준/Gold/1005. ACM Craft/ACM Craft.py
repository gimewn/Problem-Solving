import sys
sys.setrecursionlimit(10**9)

def cal_time():

    def do_seq(now):
        nonlocal seq

        if DP[now] >= 0:
            return DP[now]

        if now not in seq:
            return time[now]

        for t in seq[now]:
            res = do_seq(t)
            if res > DP[now]:
                DP[now] = res

        DP[now] += time[now]

        return DP[now]

    N, K = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    seq = {}
    DP = [-1]*(N+1)

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        if Y not in seq:
            seq[Y] = set()
        seq[Y].add(X)

    W = int(sys.stdin.readline())

    if W in seq:
        do_seq(W)
        print(DP[W])
    else:
        print(time[W])

T = int(input())

for _ in range(T):
    cal_time()