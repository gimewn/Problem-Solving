import sys, heapq

inputs = sys.stdin.readline

N, L = map(int, inputs().split())

puddle = [list(map(int, inputs().split())) for _ in range(N)]

answer = 0

puddle.sort()

prev = 0

for start, end in puddle:
    # 그 전 널빤지가 이번 웅덩이를 전부 덮고 있으면
    # 새로 덮어줄 필요 없음
    if prev > end:
        continue

    # 그 전 널빤지가 이번 웅덩이에 걸쳐 있으면
    # start를 걸쳐 있는 부분으로 세팅
    if prev > start:
        start = prev
    
    # 널빤지 몇 개 세팅해야 하는지 구하기
    count = (end-start) // L
    left = (end-start) % L
    
    if left:
        count += 1

    answer += count

    # 널빤지가 덮고 있는 마지막 위치 갱신
    prev = start + count*L

print(answer)