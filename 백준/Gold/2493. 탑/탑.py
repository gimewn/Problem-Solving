N = int(input())
castle = list(map(int, input().split(" ")))
stack = []
answer = [0]*N

for idx in range(N):
    while stack:
        if castle[idx] < stack[-1][1]:
            answer[idx] = stack[-1][0]
            break
        else:
            stack.pop()
    stack.append((idx+1, castle[idx]))

print(*answer)