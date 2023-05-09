import sys

input = sys.stdin.readline

H, K, R = map(int, input().split())

node = 1

for height in range(1, H+1):
    node += 2**height

intern = []

for _ in range(2**H):
    intern.append(list(map(int, input().split())))

left_work = [[] for _ in range(node - 2**H)]
right_work = [[] for _ in range(node - 2**H)]

answer = 0

for day in range(1, R+1):
    # 보스의 일
    # 짝수날이면
    if day % 2 == 0:
        # 보스의 오른쪽 부하에서 온 일 처리
        if right_work[0]:
            # 처리해서 answer에 더해줌
            answer += right_work[0].pop(0)
    # 홀수날이면
    elif day % 2 == 1:
        # 보스의 왼쪽 부하에서 온 일 처리
        if left_work[0]:
            # 처리해서 answer에 더해줌
            answer += left_work[0].pop(0)

    # 보스 X && 말단 X인 직원들의 일
    for idx in range(1, node - 2**H):
        # 홀수날이고
        if day % 2 == 1:
            # 내가 홀수(왼쪽)이고, 내 왼쪽에 일이 있으면
            if idx % 2 == 1 and left_work[idx]:
                # 상사의 왼쪽 일 리스트에 내 왼쪽 일 보내기
                left_work[(idx-1)//2].append(left_work[idx].pop(0))
            # 내가 짝수(오른쪽)이고, 내 왼쪽에 일이 있으면
            elif idx % 2 == 0 and left_work[idx]:
                # 상사의 오른쪽 일 리스트에 내 왼쪽 일 보내기
                right_work[(idx-1)//2].append(left_work[idx].pop(0))
        # 짝수날이고
        elif day % 2 == 0:
            # 내가 홀수(왼쪽)이고, 내 오른쪽에 일이 있으면
            if idx % 2 == 1 and right_work[idx]:
                # 상사의 왼쪽 일 리스트에 내 오른쪽 일 보내기
                left_work[(idx-1)//2].append(right_work[idx].pop(0))
            # 내가 짝수(오른쪽)이고, 내 오른쪽에 일이 있으면
            elif idx % 2 == 0 and right_work[idx]:
                # 상사의 오른쪽 일 리스트에 내 오른쪽 일 보내기
                right_work[(idx-1)//2].append(right_work[idx].pop(0))

    # 말단 직원의 일
    for idx in range(2**H):
        # 트리에서의 인덱스
        intern_idx = (node-2**H+idx)
        # 처리해야 할 일이 있으면
        if intern[idx]:
            # 내가 홀수(왼쪽이면)
            if intern_idx % 2 == 1:
                # 상사의 왼쪽 일 리스트에 내 일 보내기
                left_work[(intern_idx-1)//2].append(intern[idx].pop(0))
            # 내가 짝수(오른쪽이면)
            elif intern_idx % 2 == 0:
                # 상사의 오른쪽 일 리스트에 내 일 보내기
                right_work[(intern_idx-1)//2].append(intern[idx].pop(0))

print(answer)