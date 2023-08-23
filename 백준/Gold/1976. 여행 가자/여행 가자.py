import sys

def find(num):
    if cities[num] != num:
        cities[num] = find(cities[num])
    return cities[num]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa != fb:
        min_f, max_f = min(fa, fb), max(fa, fb)
        cities[max_f] = min_f

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

cities = [num for num in range(N+1)]

for idx in range(1, N+1):
    connect = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if connect[j]:
            union(idx, j+1)

route = list(map(int, sys.stdin.readline().split()))

answer = 'YES'

for idx in range(1, M):
    if cities[route[idx]] != cities[route[idx-1]]:
        answer = 'NO'
        break

print(answer)