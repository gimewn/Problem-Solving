import sys

def find(num):
    if robots[num] != num:
        robots[num] = find(robots[num])
    return robots[num]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return

    if fa not in robot_count:
        robot_count[fa] = 1
    if fb not in robot_count:
        robot_count[fb] = 1

    if fa < fb:
        robots[fb] = fa
        robot_count[fa] += robot_count[fb]
        robot_count[fb] = 0
    else:
        robots[fa] = fb
        robot_count[fb] += robot_count[fa]
        robot_count[fa] = 0

N = int(sys.stdin.readline())
robots = [num for num in range(10**6 + 1)]
robot_count = {}

for _ in range(N):
    temp = list(sys.stdin.readline().split())
    if temp[0] == 'I':
        union(int(temp[1]), int(temp[2]))
    elif temp[0] == 'Q':
        num = int(temp[1])
        fnum = find(num)
        if fnum not in robot_count:
            print(1)
        else:
            print(robot_count[fnum])