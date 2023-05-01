import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))

A = list(map(int, input().split(" ")))

doubleN = N*2

state = [True]*(N)

waste, now = 0, 1

while True:
    # 한 바퀴 회전
    A = [A[-1]] + A[:-1]
    state = [state[-1]] + state[:-1]
    state[-1] = True

    # 로봇 위치 옮기기
    for idx in range(N-2, -1, -1):
        if state[idx] == False:
            if state[idx+1] == True and A[idx+1] > 0:
                state[idx] = True
                state[idx+1] = False
                A[idx+1] -= 1
                if A[idx+1] == 0:
                    waste += 1

    state[-1] = True

    if state[0] and A[0] > 0:
        state[0] = False
        A[0] -= 1
        if A[0] == 0:
            waste += 1

    if waste >= K:
        print(now)
        break
    now += 1