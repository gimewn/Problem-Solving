import sys

def find(num):
    if num != friend_info[num]:
        friend_info[num] = find(friend_info[num])
    return friend_info[num]

def union(a, b, fa, fb):
    if friend_cost[fa] <= friend_cost[fb]:
        friend_info[b] = fa
        for idx in range(1, N+1):
            if friend_info[idx] == fb:
                friend_info[idx] = fa
    else:
        friend_info[a] = fb
        for idx in range(1, N+1):
            if friend_info[idx] == fa:
                friend_info[idx] = fb

N, M, K = map(int, sys.stdin.readline().split())

friend_cost = [0] + list(map(int, sys.stdin.readline().split()))
friend_info = [0] + [num for num in range(1, N+1)]
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    fa, fb = find(a), find(b)
    if fa != fb:
        union(a, b, fa, fb)

for friend in set(friend_info):
    answer += friend_cost[friend]
    if answer > K:
        print('Oh no')
        exit(0)
print(answer)