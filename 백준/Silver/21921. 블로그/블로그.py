import sys
from collections import defaultdict
input = sys.stdin.readline

N, X = map(int, input().split(" "))
visit = list(map(int, input().split(" ")))

now = sum(visit[:X])
answer = now
cnt = 1

for idx in range(N-X):
    now -= visit[idx]
    now += visit[idx+X]

    if now > answer:
        answer = now
        cnt = 1
    elif now == answer:
        cnt += 1

if answer > 0:
    print(answer)
    print(cnt)
else:
    print('SAD')