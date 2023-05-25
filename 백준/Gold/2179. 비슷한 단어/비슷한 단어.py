import sys

n = int(sys.stdin.readline())

word_dict = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    for idx in range(len(word), 0, -1):
        temp = word[:idx]
        if idx in word_dict:
            if temp in word_dict[idx]:
                word_dict[idx][temp].append(word)
            else:
                word_dict[idx][temp] = [word]
        else:
            word_dict[idx] = {
                temp: [word]
            }

word_dict_key = sorted(list(word_dict.keys()), reverse=True)
flag = False

for length in word_dict_key:
    for w in word_dict[length]:
        if len(word_dict[length][w]) >= 2:
            print(word_dict[length][w][0])
            print(word_dict[length][w][1])
            flag = True
            break
    if flag:
        break
