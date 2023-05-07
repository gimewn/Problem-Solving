import math
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

gym = [float('inf')]*(N+1)

road = {}

for _ in range(M):
    A, B, C = map(int, input().split())
    if A in road:
        road[A].append((B, C))
    else:
        road[A] = [(B, C)]
    if B in road:
        road[B].append((A, C))
    else:
        road[B] = [(A, C)]

def is_prime_number(number):
    # 에라토스테네스의 체로 number*2 범위까지 소수 검사
    check = [0]*(number*2+1)

    for num in range(2, int(math.sqrt(number*2))+1):
        if check[num] == 0:
            idx = 2
            while num*idx <= number*2:
                check[num*idx] = 1
                idx += 1

    return check

def dijkstra(start):
    gym[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, next = heapq.heappop(heap)

        if cost > gym[next]:
            continue

        for i in road[next]:
            # x레벨 미만으로는 접근 불가 => 출발지 레벨, 경유지 레벨 중 더 높은 레벨로
            i_cost = max(cost, i[1])
            if i_cost < gym[i[0]]:
                gym[i[0]] = i_cost
                heapq.heappush(heap, (i_cost, i[0]))

# dijkstra 알고리즘으로 각 체육관까지 가는 최소 레벨 구하기
dijkstra(1)

# ㅇㅇ레벨 미만 => N번째 체육관까지 가는데 필요한 레벨 +1의 *2까지 소수인지 검사
check_prime = is_prime_number(gym[-1]+1)

# 마지막 체육관까지 가는데 필요한 레벨 +1부터 돌면서 소수인 것 찾기
for idx in range(gym[-1]+1, (gym[-1]*2)+1):
    if check_prime[idx] == 0:
        print(idx)
        sys.exit()