from collections import deque

words = input()
bomb = list(input())

bomb_len = len(bomb)

stack = []
stack_len = 0

for idx in range(len(words)):
    stack.append(words[idx])
    stack_len += 1
    if stack_len >= bomb_len:
        if stack[stack_len-bomb_len:] == bomb:
            for _ in range(bomb_len):
                stack.pop()
            stack_len -= bomb_len

if stack:
    print(''.join(stack))
else:
    print("FRULA")