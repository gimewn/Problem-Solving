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
            # 만약 k번째 좌표가 기준 행과 기준 행 + l 사이이고, 기준 열과 기준 열 + l 사이라면
            # 막을 수 있으므로 defense ++
            for k in range(K):
                kx, ky = stars[k]
                if ix <= kx <= ix+L and jy <= ky <= jy+L:
                    defense += 1
                # x좌표가 기준 행 + l 보다 커짐 => 뒤에 것들은 볼 필요 없음
                elif kx > ix+L:
                    break
            # answer와 별똥별 개수에서 방어한 개수 뺀 것을 비교하여 갱신
            answer = min(answer, K-defense)

    print(answer)

if __name__ == "__main__":
    main()