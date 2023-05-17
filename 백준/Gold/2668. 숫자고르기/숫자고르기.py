N = int(input())

top_num = [num for num in range(1, N+1)]
under_num = [int(input()) for _ in range(N)]
set_under = set(under_num)
under_dict = {}

for idx in range(N):
    if under_num[idx] not in under_dict:
        under_dict[under_num[idx]] = set()
    under_dict[under_num[idx]].add(top_num[idx])

check = [1]*N

while True:
    flag = False
    for idx in range(N):
        if check[idx]:
            if top_num[idx] not in under_dict or not len(under_dict[top_num[idx]]):
                under_dict[under_num[idx]].remove(top_num[idx])
                check[idx] = 0
                flag = True
                if not len(under_dict[under_num[idx]]):
                    del under_dict[under_num[idx]]
    if not flag:
        break

print(len(under_dict.keys()))
key = sorted(under_dict.keys())
print(*key, sep="\n")
