n = int(input())

building = [list(map(int, input().split())) for _ in range(n)]
building = building + [[building[-1][0]+1, 0]]
answer = 0
stack = [0]

for b in building:
    # 새로 들어온 값이 스택의 마지막 값보다 적다 => 건물 하나가 끝났다
    if b[1] < stack[-1]:
        height = b[1]
        # 들어온 값이 스택의 마지막 값보다 작을 경우에만
        while b[1] < stack[-1]:
            # height와 스택의 마지막 값이 같지 않다면
            if height != stack[-1]:
                # 건물 수 더해주기
                answer += 1
                # 높이 갱신
                height = stack[-1]
            # height, stack[-1] 같은지 관계없이 pop 해주기 => 새로 들어온 값보다 같거나 큰 값 없애주기
            stack.pop()
    # stack에 값 넣어주기
    stack.append(b[1])

print(answer)