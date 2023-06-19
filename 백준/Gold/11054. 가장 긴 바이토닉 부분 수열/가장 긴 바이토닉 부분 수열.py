import sys

def cal_DP(istart, iend, ioffset, jstart, joffset):
    DP = [0]*N

    for i in range(istart, iend, ioffset):
        for j in range(jstart, i, joffset):
            if lst[i] > lst[j]:
                DP[i] = max(DP[i], DP[j] + 1)

    return DP

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

DP_max = [0]*N
DP_min = [0]*N

answer = 0

# 증가하는 수열 구하기
# 1번째 수부터 탐색
# 나보다 앞에 있으면서 작은 수의 개수 세기
DP_max = cal_DP(1, N, 1, 0, 1)

# 감소하는 수열 구하기
# 뒤에서 2번째 수부터 역순으로 탐색
# 나보다 뒤에 있으면서 작은 수의 개수 세기
DP_min = cal_DP(N-2, -1, -1, N-1, -1)

for idx in range(N):
    # 나보다 앞에 있는 작은 수 개수 + 나보다 뒤에 있는 작은 수 개수
    answer = max(DP_max[idx]+DP_min[idx], answer)

# 자기 자신 +1
print(answer+1)
