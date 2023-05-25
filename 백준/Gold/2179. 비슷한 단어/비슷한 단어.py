import sys

def cal(one, two):
    global answer
    if len(one) <= len(two):
        limit = len(one)
        target = two
        start = one
    elif len(two) < len(one):
        limit = len(two)
        target = one
        start = two

    for idx in range(limit, 0, -1):
        if idx <= answer:
            return False
        if target.startswith(start[:idx]):
            if idx > answer:
                answer = idx
                return idx

n = int(sys.stdin.readline())
answer = -1
S, T = '', ''

words = []
ans_words = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)

for i in range(n-1):
    for j in range(i+1, n):
        res = cal(words[i], words[j])
        if res:
            ans_words = (words[i], words[j])

print(ans_words[0])
print(ans_words[1])