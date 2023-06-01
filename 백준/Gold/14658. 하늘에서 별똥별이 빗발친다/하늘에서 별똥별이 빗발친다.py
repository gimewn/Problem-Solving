import sys
from collections import deque

def main():

    N, M, L, K = map(int, sys.stdin.readline().split())

    stars = []

    # 기본 값 => 별똥별 개수
    answer = K

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        stars.append((x, y))

    stars.sort(key=lambda key: (key[0], key[1]))

    # 행 기준점
    for i in range(K):
        ix, iy = stars[i]
        # 열 기준 점
        for j in range(K):
            defense = 0
            jx, jy = stars[j]
            # ix와 jx 중 더 작은 값
            minx = min(ix, jx)
            # iy와 jy 중 더 작은 값
            miny = min(iy, jy)
            # 만약 k번째 좌표의 x가 minx 와 minx+l 사이이고
            # y가 miny와 miny+l 사이라면
            # 막을 수 있으므로 defense ++
            for k in range(K):
                kx, ky = stars[k]
                if minx <= kx <= minx+L and miny <= ky <= miny+L:
                    defense += 1
                # x좌표가 minx + l 보다 커짐 => 뒤에 것들은 볼 필요 없음
                elif kx > minx+L:
                    break
            # answer와 별똥별 개수에서 방어한 개수 뺀 것을 비교하여 갱신
            answer = min(answer, K-defense)

    print(answer)

if __name__ == "__main__":
    main()
