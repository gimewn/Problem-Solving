from collections import deque

S = input()
T = input()

diff = len(T) - len(S)

def BFS():
    q = deque()
    q.append((T, 0))
    visit = set()
    while q:
        now, cnt = q.popleft()

        if now == S:
            return 1

        if cnt > diff:
            return 0

        if now[-1] == 'A' and now[:-1] not in visit:
            visit.add(now[:-1])
            q.append((now[:-1], cnt+1))

        if now[0] == 'B' and now[1:][::-1] not in visit:
            visit.add(now[1:][::-1])
            q.append((now[1:][::-1], cnt+1))

    return 0

print(BFS())