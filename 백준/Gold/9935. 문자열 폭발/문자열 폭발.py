words = input()
bomb = list(input())

bomb_len = len(bomb)

stack = []
stack_len = 0

for idx in range(len(words)):
    # words의 문자열을 하나씩 stack에 담아준다.
    stack.append(words[idx])
    # stack의 길이 +1
    stack_len += 1
    # stack의 길이가 폭탄의 길이 이상이면
    if stack_len >= bomb_len:
        # 끝에서부터 폭탄 길이만큼 뽑아와서 폭탄과 같은지 검사
        if stack[stack_len-bomb_len:] == bomb:
            # 같다면 폭탄 길이만큼 pop해준다.
            for _ in range(bomb_len):
                stack.pop()
            # stack 길이에서 폭탄 길이만큼 빼준다.
            stack_len -= bomb_len

# stack에 문자열이 남아 있으면 출력
if stack:
    print(''.join(stack))
# 남아 있지 않으면 FRULA 출력
else:
    print("FRULA")