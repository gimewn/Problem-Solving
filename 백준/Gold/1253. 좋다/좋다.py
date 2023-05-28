from collections import deque

n = int(input())

nums = list(map(int, input().split()))
check = [0]*n

distict_nums = {}

answer = 0

# nums의 각 숫자에 대해 딕셔너리로 해당 숫자의 개수와 등장하는 index 기록
for idx in range(n):
    if nums[idx] in distict_nums:
        distict_nums[nums[idx]].add(idx)
    else:
        distict_nums[nums[idx]] = set()
        distict_nums[nums[idx]].add(idx)

# 두 개씩 숫자의 합을 확인하며
for i in range(n-1):
    for j in range(i+1, n):
        cal = nums[i] + nums[j]
        if cal in distict_nums:
            temp = set()
            # 해당 숫자의 인덱스 중 i 및 j와 일치하지 않는 인덱스를 temp에 담기
            for idx in distict_nums[cal]:
                if idx != i and idx != j:
                    temp.add(idx)
            # temp의 개수를 answer에 더함
            answer += len(temp)
            # 해당 숫자의 인덱스 set을 temp를 제거한 것으로 갱신
            distict_nums[cal] = distict_nums[cal] ^ temp
print(answer)