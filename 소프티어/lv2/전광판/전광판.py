import sys

input = sys.stdin.readline

# 0 ~ 9 숫자별 켜지면 안 되는 전구

num = [[7], [1, 4, 5, 6, 7], [3, 6], [5, 6], [1, 4, 5], [2, 5], [2], [4, 5 , 7], [], [5]]

lights = [[0]*8 for _ in range(11)]

# lights에 각 숫자별 7개의 전구 상태 담아주기 (마지막(-1번째) = 하나도 켜지지 않은 상태)
for idx in range(10):
    for switch in range(1, 8):
        if switch not in num[idx]:
            lights[idx][switch] = 1

def cal_switch(now, next):
    # 현재 숫자와 바꿔야 할 숫자가 같으면 스위치 켜줄 필요 없음
    if now == next:
        return 0

    res = 0
    # 1번부터 7번 전구까지 비교
    # 만약 꺼져 있어야 하는데 켜져 있거나, 켜져 있어야 하는데 꺼져 있으면
    # 스위치 조작 횟수 증가
    for switch in range(1, 8):
        if lights[next][switch] == 0 and lights[now][switch] == 1:
            res += 1
        elif lights[next][switch] == 1 and lights[now][switch] == 0:
            res += 1

    return res

T = int(input())

for _ in range(T):
    answer = 0
    A, B = input().split()
    A = list(map(int, A))
    B = list(map(int, B))

    length = max(len(A), len(B))

    # 길이 맞춰주기, 짧은 쪽에 -1 추가
    if len(A) < len(B):
        A = [-1]*(length-len(A)) + A
    elif len(B) < len(A):
        B = [-1]*(length-len(B)) + B

    # 뒤에서부터 현재 숫자와 바꿔야하는 숫자 함수 넘겨주기
    for idx in range(length - 1, -1, -1):
        answer += cal_switch(A[idx], B[idx])

    print(answer)