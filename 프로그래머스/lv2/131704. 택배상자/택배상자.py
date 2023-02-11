def solution(order):
    answer = 0
    length = len(order)
    stack = []
    idx = 1

    while idx <= length:
        stack.append(idx)
        # stack의 가장 최근 넣은 상자와 order의 첫번째 상자가 같으면
        if stack[-1] == order[answer]:
            while stack and order and stack[-1] == order[answer]:
                stack.pop()
                answer += 1
        idx += 1

    return answer