import sys

def main():

    def DP():
        for idx in range(D + 1):
            if idx > 0:
                road[idx] = min(road[idx], road[idx - 1] + 1)
            # 현재 위치에서 시작하는 지름길이 있으면
            if idx in short_road:
                # 끝나는 지점들을 가지고
                for end in short_road[idx]:
                    # 현재 지점 + 지름길 길이가 지름길 끝나는 위치보다 작으면
                    if road[idx] + short_road[idx][end] < road[end]:
                        # 갱신
                        road[end] = road[idx] + short_road[idx][end]

    N, D = map(int, sys.stdin.readline().split())

    road = [num for num in range(D+1)]

    short_road = {}

    road[0] = 0

    for _ in range(N):
        start, end, length = map(int, sys.stdin.readline().split())
        if length < end-start and end <= D:
            if start not in short_road:
                short_road[start] = {}
            if end not in short_road[start]:
                short_road[start][end] = 2e9

            short_road[start][end] = min(short_road[start][end], length)

    DP()

    print(road[-1])

if __name__ == '__main__':
    main()