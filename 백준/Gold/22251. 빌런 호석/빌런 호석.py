N, K, P, X = map(int, input().split())

number = {
    '0': {num for num in range(6)},
    '1': {1, 2},
    '2': {0, 1, 3, 4, 6},
    '3': {0, 1, 2, 3, 6},
    '4': {1, 2, 5, 6},
    '5': {0, 2, 3, 5, 6},
    '6': {0, 2, 3, 4, 5, 6},
    '7': {0, 1, 2},
    '8': {num for num in range(7)},
    '9': {0, 1, 2, 3, 5, 6}}

answer = 0

def cal(now, target):
    return len(number[now]^number[target])

def DFS(level, cnt, floor):
    global answer
    if cnt > P:
        return
    if level == K:
        if 1 <= cnt <= P:
            word = ''.join(floor)
            if '0'*K < word <= str_N:
                answer += 1
        return

    if level == 0:
        limit = int(str_N[level])
    else:
        limit = 9

    for num in range(limit+1):
        temp = cal(str_X[level], str(num))
        DFS(level+1, cnt+temp, floor+str(num))

str_N = '0'*(K-len(str(N))) + str(N)
str_X = '0'*(K-len(str(X))) + str(X)

DFS(0, 0, '')

print(answer)