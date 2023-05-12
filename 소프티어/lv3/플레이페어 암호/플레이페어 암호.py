import sys
from collections import defaultdict, deque

input = sys.stdin.readline

message = input().rstrip()
key = input().rstrip()

alphabet = [0]*(ord('Z') - ord('A')+1)
where_alp = defaultdict(list)
board = [[0]*5 for _ in range(5)]

y, x = 0, 0

for k in key:
    ord_num = ord(k) - ord('A')
    # 아직 등장하지 않았다면
    if not alphabet[ord_num]:
        # 기록
        alphabet[ord_num] = 1
        # 5*5 보드에 채워주기
        board[y][x] = k
        # 알파벳의 위치 기록
        where_alp[k] = [y, x]
        x += 1
        # x가 5라면 다음 행으로
        if x == 5:
            y += 1
            x = 0

for idx in range(len(alphabet)):
    # 중복이라 보드에 채워지지 않았다면
    if not alphabet[idx]:
        alp = chr(ord('A')+idx)
        # J는 무시
        if alp == 'J':
            continue
        # 보드에 채워주기
        board[y][x] = alp
        # 알파벳의 위치 기록
        where_alp[alp] = [y, x]
        x += 1
        # x가 5라면 다음 행으로
        if x == 5:
            y += 1
            x = 0

stack = deque()
message = deque(message)

idx = 0

while message:
    # stack에 message의 첫 번째 원소 담기
    stack.append(message.popleft())
    idx += 1
    if message:
        # 만약 홀수라면 => 다음 원소와 같을 경우 처리 필요 (2개씩 끊기 때문에)
        if idx % 2 == 1 and stack[-1] == message[0]:
            # X 쌍이라면 => 다음 원소 사이에 Q 넣기
            if stack[-1] == 'X':
                stack.append('Q')
                idx += 1
            # X 외 알파벳 쌍이라면 => 다음 원소 사이에 X 넣기
            else:
                stack.append('X')
                idx += 1
# 만약 한 글자가 남았다면 => X 넣기
if len(stack) % 2 == 1:
    stack.append('X')

answer = ''

while stack:
    # 2개씩 끊기
    first = stack.popleft()
    second = stack.popleft()

    fy, fx = where_alp[first][0], where_alp[first][1]
    sy, sx = where_alp[second][0], where_alp[second][1]

    # 행이 같다면 => 열을 오른쪽으로
    if fy == sy:
        fx = (fx+1) % 5
        sx = (sx+1) % 5
    # 열이 같다면 => 행을 아래쪽으로
    elif fx == sx:
        fy = (fy+1) % 5
        sy = (sy+1) % 5
    # 행과 열 모두 다르다면 => 서로 열 바꾸기
    else:
        fx, sx = sx, fx

    answer += board[fy][fx]
    answer += board[sy][sx]

print(answer)