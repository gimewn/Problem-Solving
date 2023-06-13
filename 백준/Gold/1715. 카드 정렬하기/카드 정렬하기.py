import sys
import heapq

def main():

    N = int(sys.stdin.readline())
    nums = []
    answer = 0

    if N == 1:
        print(0)
        exit(0)

    for _ in range(N):
        num = int(sys.stdin.readline())
        heapq.heappush(nums, num)

    while len(nums) > 1:
        one = heapq.heappop(nums)
        two = heapq.heappop(nums)
        answer += one + two
        heapq.heappush(nums, one + two)

    print(answer)


if __name__ == '__main__':
    main()