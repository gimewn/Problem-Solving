def solution(n, m, section):
    answer = 1

    start = section[0] + m - 1

    while section:
        if section[0] <= start:
            section.pop(0)
        else:
            answer += 1
            start = section[0] + m - 1

    return answer