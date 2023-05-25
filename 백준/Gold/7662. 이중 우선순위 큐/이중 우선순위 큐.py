import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    both_del = [0]*n

    for idx in range(n):
        operation, number = sys.stdin.readline().split()
        if operation == 'I':
            heapq.heappush(max_heap, (int(number)*-1, idx))
            heapq.heappush(min_heap, (int(number), idx))
            both_del[idx] = 1

        elif operation == 'D':
            if number == '-1':
                # max_heap에서 제거된 요소 제거해주기 => both_del의 idx가 0이면 => max_heap에서 지워진 것
                while min_heap and not both_del[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    temp = heapq.heappop(min_heap)
                    both_del[temp[1]] = 0
            elif number == '1':
                # min_heap에서 제거된 요소 제거해주기 => both_del의 idx가 0이면 => min_heap에서 지워진 것
                while max_heap and not both_del[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    temp = heapq.heappop(max_heap)
                    both_del[temp[1]] = 0

    while min_heap and not both_del[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not both_del[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if sum(both_del):
        max_value = heapq.heappop(max_heap)
        min_value = heapq.heappop(min_heap)
        print(-1*max_value[0], min_value[0])
    else:
        print("EMPTY")