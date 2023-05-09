import math
import sys

input = sys.stdin.readline

def cal(num):
    cost = 0
    # power를 돌면서 num으로 성능을 올리기까지 필요한 비용 계산
    for p in power:
        # num보다 작다면 => 비용 계산
        if p < num:
            cost += (num-p)**2
    # 총 비용이 B를 초과할 경우 => 성능 향상 불가
    if cost > B:
        return False
    # 이하일 경우 => 성능 향상 가능
    elif cost <= B:
        return True

N, B = map(int, input().split())

power = list(map(int, input().split()))

answer = 0

# end = 성능의 제한조건 내 최대값
start, end = 0, max(power)+int(math.sqrt(10**18))

while start <= end:
    mid = (start+end)//2

    res = cal(mid)

    # 비용이 B 초과이면 => end값 줄이기
    if not res:
        end = mid-1
    # 비용이 B 이하이면 => start값 늘려서 확인
    else:
        start = mid+1
        answer = mid

print(answer)