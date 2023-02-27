import sys

input = sys.stdin.readline

def find(num):
    # num과 dot[num]이 일치 => 자기 자신
    if num == dot[num]:
        return num
    # 연결된 노드 찾아주기
    dot[num] = find(dot[num])
    return dot[num]


def union(n1, n2):
    f1, f2 = find(n1), find(n2)
    # 일치 => 연결되어 있음(사이클 발견)
    if f1 == f2:
        return True
    dot[max(f1, f2)] = min(f1, f2)

n, m = map(int, input().split())

dot = [num for num in range(n)]

answer = 0

for idx in range(1, m+1):
    d1, d2 = map(int, input().split())
    if union(d1, d2):
        answer = idx
        break

print(answer)
