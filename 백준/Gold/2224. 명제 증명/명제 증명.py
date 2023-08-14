import sys, heapq

def dijkstra(start):
    global answer
    trues = set()
    heap = []
    heapq.heappush(heap, start)

    while heap:
        now = heapq.heappop(heap)

        if now not in alphabet_dict:
            continue

        for next_value in alphabet_dict[now]:
            if (start, next_value) not in trues and next_value != start:
                trues.add((start, next_value))
                heapq.heappush(heap, next_value)

    answer = set.union(answer, trues)


N = int(sys.stdin.readline())

alphabet_dict = dict()
answer = set()

for _ in range(N):
    forward, mark, backward = sys.stdin.readline().rstrip().split()
    if forward == backward:
        continue
    if forward in alphabet_dict:
        alphabet_dict[forward].append(backward)
    else:
        alphabet_dict[forward] = [backward]

alphabet_keys = sorted(alphabet_dict.keys())

for key in alphabet_keys:
    dijkstra(key)

answer = sorted(answer)

print(len(answer))

for a, b in answer:
    print(f'{a} => {b}')