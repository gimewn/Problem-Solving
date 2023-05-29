H, W = map(int, input().split())

block = list(map(int, input().split()))
answer = 0
left = [False]*W
right = [False]*W

def find_max(dir, now):

    if dir == 'left':
        max_value = -2e9
        max_idx = -1
        for idx in range(now):
            if block[idx] > max_value:
                max_value = block[idx]
                max_idx = idx
        return max_idx

    elif dir == 'right':
        max_value = -2e9
        max_idx = -1
        for idx in range(now+1, W):
            if block[idx] > max_value:
                max_value = block[idx]
                max_idx = idx
        return max_idx


for idx in range(1, W-1):
    if not left[idx-1]:
        left[idx] = find_max('left', idx)
    else:
        left[idx] = left[idx-1]
    if not right[idx-1]:
        right[idx] = find_max('right', idx)
    else:
        right[idx] = right[idx-1]

    temp = min(block[left[idx]], block[right[idx]]) - block[idx]

    if temp > 0:
        answer += temp

    if block[left[idx]] < block[idx]:
        left[idx] = idx
    if right[idx] <= idx:
        right[idx] = find_max('right', idx)

print(answer)