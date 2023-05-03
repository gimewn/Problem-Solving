import sys
import heapq

input = sys.stdin.readline

W, N = map(int, input().split())

heap = []

# Heap => 정렬할 시 시간초과
# price (1차 내림차순 -> - ), weight (2차 내림차순 -> - )
for _ in range(N):
    weight, price = list(map(int, input().split()))
    heapq.heappush(heap, [-price, -weight])

answer = 0
idx = 0

while W and idx < N:
    max_price, max_weight = heapq.heappop(heap)
    max_price *= -1
    max_weight *= -1

    if max_weight <= W:
        W -= max_weight
        answer += max_price * max_weight
    else:
        answer += W * max_price
        break

    idx += 1

print(answer)