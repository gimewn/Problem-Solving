from collections import deque

n, k = map(int, input().split())

def BFS(start):
    q = deque()
    q.append((start, 0))
    visit = [0]*100001
    visit[start] = 1

    while q:
        now, time = q.popleft()

        if now == k:
            return time

        cal = [now+1, now-1, now*2]

        for c in cal:
            if 0 <= c <= 100000 and not visit[c]:
                visit[c] = 1
                if c == now*2:
                    q.appendleft((c, time))
                else:
                    q.append((c, time+1))

print(BFS(n))