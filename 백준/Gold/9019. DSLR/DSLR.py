import sys
from collections import deque

t = int(sys.stdin.readline())

def dslr(num):
    return [['D', (num * 2) % 10000], ['S', (num-1) % 10000],
            ['L', num // 1000 + (num % 1000) * 10], ['R', (num % 10) * 1000 + num // 10]]

def make_A_to_B(now, target):
    q = deque([(now, '')])
    check = [False]*10001
    check[now] = True

    while q:
        value, command = q.popleft()

        if value == target:
            return command

        for ncommand, nvalue in dslr(value):
            if not check[nvalue]:
                check[nvalue] = True
                check[nvalue] = command + ncommand
                q.append((nvalue, check[nvalue]))

for _ in range(t):

    A, B = map(int, sys.stdin.readline().split())
    print(make_A_to_B(A, B))