import sys
import heapq

sys.setrecursionlimit(10**5)

def main():

    def prim(start):
        answer = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            cost, num = heapq.heappop(heap)
            if not check[num]:
                check[num] = 1
                answer += cost
                for i in range(N):
                    if num != i and not check[i]:
                        heapq.heappush(heap, (board[num][i], i))
        return answer


    N = int(sys.stdin.readline())

    planets = []
    check = [0]*N
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(prim(0))

if __name__ == '__main__':
    main()