import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    answer = 1
    word = []
    for _ in range(n):
        tel = sys.stdin.readline().rstrip()
        heapq.heappush(word, tel)

    prev = ''

    while word:
        now = heapq.heappop(word)
        if prev:
            if now.startswith(prev):
                answer = 0
                break
        prev = now

    if answer:
        print("YES")
    else:
        print("NO")