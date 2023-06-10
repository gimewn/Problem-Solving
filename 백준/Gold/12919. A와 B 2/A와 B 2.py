import sys

def bfs(start, end):
    q = set()
    q.add(start)

    while q:
        now = q.pop()
        if now == end:
            return 1

        if not now: continue

        if now[-1] == 'A':
            q.add(now[:-1])

        if now[0] == 'B':
            q.add(now[1:][::-1])

    return 0

def main():
    S = sys.stdin.readline().rstrip()
    T = sys.stdin.readline().rstrip()

    print(bfs(T, S))

if __name__ == '__main__':
    main()