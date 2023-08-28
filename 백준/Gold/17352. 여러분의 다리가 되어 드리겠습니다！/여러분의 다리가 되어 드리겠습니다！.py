import sys

def find(num):
    if num != islands[num]:
        islands[num] = find(islands[num])
    return islands[num]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return
    if fa < fb:
        islands[fb] = fa
    else:
        islands[fa] = fb

N = int(sys.stdin.readline())

islands = [0] + [num for num in range(1, N+1)]

for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

islands_set = set()

for i in islands[1:]:
    fi = find(i)
    if fi not in islands_set:
        islands_set.add(fi)

print(*islands_set)