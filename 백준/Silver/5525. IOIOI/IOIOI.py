import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
Pn = 'IO'*N + 'I'
S = sys.stdin.readline().rstrip()

start, end = 0, 2*N
word = S[:end+1]
answer = 0

while True:
    if word == Pn:
        answer += 1
    word = word[1:]
    start += 1
    end += 1
    if end >= M:
        break
    word = word + S[end]

print(answer)