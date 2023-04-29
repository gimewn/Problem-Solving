import sys

N, K = map(int, sys.stdin.readline().split())

line = list(sys.stdin.readline().rstrip())
robot = []
check = [0]*N
answer = 0

for idx in range(N):
    # 로봇이면
    if line[idx] == 'P':
        # 좌측 제일 먼 거리부터 탐색
        for next in range(idx-K, idx+K+1):
            # 범위 내이고
            if next >= 0 and next < N:
                # 부품이면
                if line[next] == 'H':
                    answer += 1
                    # 집었음을 표시하기 위해 문자 바꿔주기
                    line[next] = 'G'
                    break

print(answer)