import sys

inputs = sys.stdin.readline

N, M = map(int, inputs().split())

lst = [0] + list(map(int, inputs().split()))

moduler = [0]*M
answer = 0
moduler[0] = 1

for idx in range(1, N+1):
    lst[idx] += lst[idx-1]
    moduler[lst[idx] % M] += 1

# (moduler[j+1] - moduler[i]) % M == 0
# (moduler[j+1] % M) - (moduler[i] % M) == 0
# moduler[j+1] % M = moduler[i] % M
# 0 ~ M-1까지 나머지마다 2개를 뽑는 경우의 수 모두 더한 것 => answer
for cnt in moduler:
    answer += cnt*(cnt-1) // 2

print(answer)