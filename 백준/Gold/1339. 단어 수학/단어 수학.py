import sys

def sum_alp_to_num():
    num = 9
    res = 0

    for value in sorted(alp_to_num.values(), reverse=True):
        res += value * num
        num -= 1

    return res

N = int(sys.stdin.readline())

words = [sys.stdin.readline().rstrip() for _ in range(N)]

alp_to_num = {}

for word in words:
    length = len(word)-1
    for idx in range(len(word)):
        if word[idx] not in alp_to_num:
            alp_to_num[word[idx]] = 0
        alp_to_num[word[idx]] += 10**(length-idx)

print(sum_alp_to_num())