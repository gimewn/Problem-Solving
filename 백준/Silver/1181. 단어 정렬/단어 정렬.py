import sys

n = int(sys.stdin.readline())

words = set(sys.stdin.readline().rstrip() for _ in range(n))

sort_words = sorted(words, key=lambda x : (len(x), x))

print(*sort_words, sep="\n")