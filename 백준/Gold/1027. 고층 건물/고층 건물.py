import math

n = int(input())

building = list(map(int, input().split()))

max_cnt = -1

def cal(idx, dir):
    if dir == 'left':
        start, end, step = idx-1, -1, -1
        prev = 2e9
    elif dir == 'right':
        start, end, step = i+1, n, 1
        prev = -2e9

    cnt = 0

    for next in range(start, end, step):
        temp = (building[next]-building[idx])/(next-idx)
        if dir == 'left':
            if temp < prev:
                cnt += 1
                prev = temp
        elif dir == 'right':
            if temp > prev:
                cnt += 1
                prev = temp
    return cnt

for i in range(n):
    max_cnt = max(max_cnt, cal(i, 'left') + cal(i, 'right'))

print(max_cnt)