import sys

input = sys.stdin.readline

n = int(input())

parking = list(enumerate(map(int, input().split())))

# (index, value) - value를 기준으로 내림차순 정렬
parking.sort(key=lambda x: -x[1])

answer = 0

for i in range(n-1):
    left = 0
    right = 0
    for j in range(i+1, n):
        # i번째 값의 인덱스보다 j번째 값의 인덱스가 작다면
        # (1, 4) (0, 3) => ai < aj ... 왼쪽에 올 수 있음
        if parking[i][0] > parking[j][0]:
            # left += 1
            left += 1
        # i번째 값의 인덱스보다 j번째 값의 인덱스가 크다면
        # (1, 4) (2, 2) => ai > aj ... 오른쪽에 올 수 있음
        elif parking[i][0] < parking[j][0]:
            # 지금까지의 left를 더해줌
            # 3 4 5 1 => 5가 i번째라면 left = 3, 4
            # 3 5 1 / 4 5 1 => left의 개수만큼 조건 만족 가능
            right += left
    answer += right

print(answer)