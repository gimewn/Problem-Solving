import sys

input = sys.stdin.readline

def find(num):
    if num == dot[num]:
        return num
    dot[num] = find(dot[num])
    return dot[num]

def union(type, n1, n2):
    f1, f2 = find(n1), find(n2)
    # type이 1이면 => 같은 집합에 포함되어 있는지 확인
    if type == 1:
        if f1 == f2:
            print("YES")
        else:
            print("NO")
    # type이 0이면 => 집합 합치기
    else:
        dot[f2] = f1

n, m = map(int, input().split())

dot = [num for num in range(n+1)]

for _ in range(m):
    type, n1, n2 = map(int, input().split())
    union(type, n1, n2)