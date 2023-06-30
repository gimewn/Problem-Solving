import sys

N, A = map(int, sys.stdin.readline().split())
res = 0
damage = 0
now = 0

for idx in range(N):
    t, a, h = map(int, sys.stdin.readline().split())
    if t == 1: # 몬스터방
        if h % A == 0: # 딱 나눠 떨어지면
            damage = -1*(((h//A)-1)*a) # 1 빼주기 (용사가 n번 공격하면 몬스터는 n-1번 공격하므로)
        else:
            damage = -1*((h//A)*a)

    elif t == 2: # 포션 방이면
        A += a # 공격력 증가

    if t == 1:
        now += damage
    elif t == 2:
        now += h

    if now > 0: # 회
        # 복된 생명력이 최대 생명력보다 큰 경우 현재 생명력 == 최대 생명력
        now = 0

    res = max(res, abs(now)) # 필요한 생명력 비교

print(res+1) # 살아 있어야 하므로 +1