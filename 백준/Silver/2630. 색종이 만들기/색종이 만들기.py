N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def check_color(y, x, n):
    global white, blue
    temp = 0
    for i in range(y, y+n):
        for j in range(x, x+n):
            temp += board[i][j]
    # 더한 값이 모두 0이면 하얀색
    if temp == 0:
        white += 1
    # 더한 값이 n**2이면 파란색
    elif temp == n**2:
        blue += 1
    else:
        # 4분할
        check_color(y, x, n//2)
        check_color(y+n//2, x, n//2)
        check_color(y, x+n//2, n//2)
        check_color(y+n//2, x+n//2, n//2)

check_color(0, 0, N)

print(white)
print(blue)