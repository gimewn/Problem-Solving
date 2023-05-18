n = int(input())

stone = list(map(int, input().split()))

answer = -1

left = 0
right = 0

# 가장 길게 연속되는 것을 찾기

for idx in range(n):
    # 1이라면 left에 +1, right -= 1
    # 1 1 2 1 => 왼쪽 기준 깨달음 지수는 2
    if stone[idx] == 1:
        left += 1
        right -= 1
    # 2라면 right에 +1, left -= 1
    # 1 1 2 1 => 오른쪽 기준 깨달음 지수는 0
    elif stone[idx] == 2:
        left -= 1
        right += 1
    # 만약 깨달음 지수가 음수가 된다면 => 다시 시작하는 게 나음
    if left < 0:
        left = 0
    if right < 0:
        right = 0
    # answer, 왼쪽 기준 깨달음 지수, 오른쪽 기준 깨달음 지수 중 최대값 갱신
    answer = max(answer, left, right)

print(answer)