from itertools import permutations
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
rails = list(map(int, input().split()))
min_work = 1e9

# 순열 구하기
per_rail = permutations(rails, N)

for rail in per_rail:
    rail_list = list(rail)
    # 회차
    turn = 0
    # 회차 통틀어 일한 무게
    all_basket = 0
    # 특정 회차에서 일한 무게
    basket = 0
    idx = 0
    # turn이 K보다 작고, min_work보다 일한 무게가 적을 때만 실행
    while turn < K and all_basket < min_work:
        # 현재 무게 + 지금까지 일한 무게가 M보다 작거나 같을 때
        if rail_list[idx] + basket <= M:
            # 무게 더해주기
            basket += rail_list[idx]
            # 맨 뒤로 보내주기
            rail_list.append(rail_list[idx])
            idx += 1
        else:
            # 무게가 M을 초과했으면 => 이번 회차 마무리
            all_basket += basket
            basket = 0
            turn += 1

    min_work = min(min_work, all_basket)

print(min_work)