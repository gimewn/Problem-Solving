import sys

def find(num):
    if num != friend_info[num]:
        friend_info[num] = find(friend_info[num])
    return friend_info[num]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    if friend_cost[fa] < friend_cost[fb]:
        friend_info[fb] = fa
    else:
        friend_info[fa] = fb

N, M, K = map(int, sys.stdin.readline().split())

friend_cost = [0] + list(map(int, sys.stdin.readline().split()))
friend_info = [0] + [num for num in range(1, N+1)]
answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

friend_set = set()

for friend in friend_info:
    ff = find(friend)
    if ff not in friend_set:
        friend_set.add(ff)
        answer += friend_cost[ff]
    if answer > K:
        print('Oh no')
        exit(0)
print(answer)