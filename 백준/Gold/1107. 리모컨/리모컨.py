import sys

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

if M:
    buttons = set(map(int, sys.stdin.readline().split()))
else:
    buttons = set()

min_push = abs(N - 100)

for channel in range(1000001):
    flag = True
    for c in str(channel):
        if int(c) in buttons:
            flag = False
            break
    if flag:
        this_push = len(str(channel)) + abs(N - channel)
        min_push = min(min_push, this_push)

print(min_push)