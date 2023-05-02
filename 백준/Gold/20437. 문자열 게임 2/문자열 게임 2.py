import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    word = input()
    K = int(input())
    possible_word = defaultdict(list)
    short = 1e9
    long = -1e9
    flag = False

    for idx in range(len(word)):
        possible_word[word[idx]].append(idx)

    for w in possible_word.keys():
        if len(possible_word[w]) >= K:
            flag = True
            for idx in range((len(possible_word[w])-K)+1):
                temp = (possible_word[w][idx+K-1] - possible_word[w][idx])+1
                short = min(short, temp)
                long = max(long, temp)

    if flag:
        print(short, long)
    else:
        print(-1)