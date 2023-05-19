n = int(input())

cnt = 0
digit = 0
prev = 0
res = set()

answer = -1

def DFS(level, limit, num):
    if level == limit:
        res.add(num)
        return

    for n in range(10):
        if (num and n < int(num[-1])) or not num:
            DFS(level+1, limit, num+str(n))

while True:
    res.clear()
    DFS(-1, digit, '')
    prev = cnt
    cnt += len(res)
    if cnt >= n:
        subscrible_res = sorted(res)
        answer = subscrible_res[n-prev-1]
        break
    if cnt and prev and cnt == prev:
        break
    digit += 1

print(answer)