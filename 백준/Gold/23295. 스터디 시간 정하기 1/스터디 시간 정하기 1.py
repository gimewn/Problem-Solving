import sys

N, T = map(int, sys.stdin.readline().split())

time = [0]*100001
max_end = 0

cnt = 0

for _ in range(N):
    K = int(sys.stdin.readline())
    for _ in range(K):
        s, e = map(int, sys.stdin.readline().split())
        # 시작점에 +1, 끝점에 -1
        time[s] += 1
        time[e] -= 1
        max_end = max(max_end, e)

# 스위핑
for idx in range(1, max_end+1):
    time[idx] += time[idx-1]

start = 0
max_satisfaction = 0
satisfaction = 0
answer = 0

for end in range(max_end+1):
    satisfaction += time[end]
    if end >= T-1:
        if satisfaction > max_satisfaction:
            max_satisfaction = satisfaction
            answer = (end - T)+1
        satisfaction -= time[start]
        start += 1

print(answer, answer + T)