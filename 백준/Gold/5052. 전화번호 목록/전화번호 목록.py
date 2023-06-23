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
        # 사전순으로 빠른 것부터 하나씩 꺼내서
        now = heapq.heappop(word)
        # 만약 prev가 있으면
        if prev:
            # now가 prev로 시작하는지(접두어인지) 확인
            if now.startswith(prev):
                # 접두어이면 answer 갱신, break
                answer = 0
                break
        prev = now

    if answer:
        print("YES")
    else:
        print("NO")