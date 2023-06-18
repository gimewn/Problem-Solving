import heapq
import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

liquid = {}

for num in lst:
    # 절대값 num이 liquid에 존재하지 않으면
    if abs(num) not in liquid:
        liquid[abs(num)] = {
            'cnt': 1,
            'real': [num]
        }
    else:
        # 존재하면 cnt + 1, real에 값 넣어주기
        liquid[abs(num)]['cnt'] += 1
        liquid[abs(num)]['real'].append(num)

keys = list(liquid.keys())

heapq.heapify(keys)

prev = 0

min_ = 2e9
answer = []

# key를 작은 순서로 하나씩 꺼내오며
while keys:
    now = heapq.heappop(keys)
    # 만약 cnt가 2라면 => -num, num이 존재
    if liquid[now]['cnt'] > 1:
        # 둘을 더한 것의 0까지의 거리와 min_ 비교
        sums = sum(liquid[now]['real'])
        if abs(0 - sums) < min_:
            min_ = abs(0 - sums)
            answer = liquid[now]['real']
    # prev가 있으면 (처음 꺼낸 key가 아니면)
    if prev:
        # prev의 cnt가 2거나 now의 cnt가 2인 경우 고려
        for i in liquid[prev]['real']:
            for j in liquid[now]['real']:
                # 더한 것의 0까지의 거리와 min_비교
                if abs(0 - (i + j)) < min_:
                    min_ = abs(0 - (i + j))
                    answer = [min(i, j), max(i, j)]
    # prev 갱신
    prev = now

print(answer[0], answer[1])
