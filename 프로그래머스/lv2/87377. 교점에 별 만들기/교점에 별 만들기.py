def solution(line):
    answer = []
    dots = set()
    length = len(line)

    def cal(line1, line2):
        nonlocal max_y, max_x, min_y, min_x
        a1, b1, c1 = line1
        a2, b2, c2 = line2

        if a1 * b2 == b1 * a2:
            return False

        x = (b1 * c2 - c1 * b2) / (a1 * b2 - b1 * a2)
        y = (c1 * a2 - a1 * c2) / (a1 * b2 - b1 * a2)

        if x.is_integer() and y.is_integer():
            return (int(y), int(x))
        return False

    for i in range(length - 1):
        for j in range(i + 1, length):
            res = cal(line[i], line[j])
            if res:
                dots.add(res)

    max_x = max(dots, key=lambda x: x[1])[1]
    min_x = min(dots, key=lambda x: x[1])[1]
    max_y = max(dots, key=lambda x: x[0])[0]
    min_y = min(dots, key=lambda x: x[0])[0]

    board = [['.']*((max_x - min_x) + 1) for _ in range((max_y - min_y) + 1)]

    for y, x in dots:
        board[y-min_y][x-min_x] = '*'

    for row in board:
        answer.append(''.join(row))

    answer.reverse()

    return answer