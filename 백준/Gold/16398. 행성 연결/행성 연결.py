import sys
import heapq

sys.setrecursionlimit(10**5)

def main():

    def find(num):
        if parents[num] == num:
            return num
        parents[num] = find(parents[num])
        return parents[num]

    def union(n1, n2):
        min_, max_ = min(n1, n2), max(n1, n2)
        parents[max_] = min_

    N = int(sys.stdin.readline())

    planets = []
    parents = [num for num in range(N)]

    answer = 0

    for y in range(N):
        lst = list(map(int, sys.stdin.readline().split()))
        for x in range(N):
            if y != x:
                heapq.heappush(planets, (lst[x], y, x))

    while planets:
        cost, y, x = heapq.heappop(planets)
        fy, fx = find(y), find(x)
        if fy != fx:
            union(fy, fx)
            answer += cost

    print(answer)

if __name__ == '__main__':
    main()