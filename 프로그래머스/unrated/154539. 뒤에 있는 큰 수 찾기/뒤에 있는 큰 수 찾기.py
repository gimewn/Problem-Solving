def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    
    for idx in range(len(numbers)):
        while stack:
            if numbers[stack[-1]] < numbers[idx]:
                s_index = stack.pop()
                answer[s_index] = numbers[idx]
            else:
                break
        stack.append(idx)

    return answer