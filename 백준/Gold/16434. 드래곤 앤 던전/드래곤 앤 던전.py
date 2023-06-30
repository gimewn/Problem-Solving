import sys

inputs = sys.stdin.readline

def fight_monster(Natk, Matk, Mhp):
    cnt = Mhp // Natk
    if Mhp % Natk == 0:
        cnt -= 1
    return -1 * (cnt * Matk)

def fight_dragon():
    N, Hatk = map(int, inputs().split())
    HcurHP = 0
    answer = 0
    
    for _ in range(N):
        t, a, h = map(int, inputs().split())
        
        if t == 1:
            HcurHP += fight_monster(Hatk, a, h)
        elif t == 2:
            Hatk += a
            HcurHP += h
        # 회복된 생명력은 최대 생명력을 넘지 않아야 문
        if HcurHP > 0:
            HcurHP = 0

        # 중간에 죽으면 안 됨
        # 방 하나 깰 때마다 필요한 HP 비교
        answer = max(answer, abs(HcurHP))

    return answer + 1

print(fight_dragon())