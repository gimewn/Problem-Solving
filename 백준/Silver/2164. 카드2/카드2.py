from collections import deque

N = int(input())

num = deque([n for n in range(1, N+1)])

while len(num) > 1:
    num.popleft()
    top = num.popleft()
    num.append(top)

print(num[0])