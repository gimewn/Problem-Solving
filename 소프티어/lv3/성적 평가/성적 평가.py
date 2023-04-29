from collections import defaultdict

# 병합 정렬 구현
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    l, h = 0, 0

    res = []

    while l < len(low) and h < len(high):
        # 더 큰 값을 res에 추가 (내림차순 정렬)
        if low[l] > high[h]:
            res.append(low[l])
            l += 1
        else:
            res.append(high[h])
            h += 1
    # 남은 값 추가
    res += low[l:]
    res += high[h:]
    
    return res

def cal_rate(lst, flag):
    # 점수 별 등수
    rate = {}
    result = []
    # 앞에 있는 사람 수
    prev = 0
    sorted_score = merge_sort(lst)
    # 내림차순으로 등수 매기기
    for ss in sorted_score:
        # 아직 등수가 없다면, 등수 등록
        if ss not in rate:
            rate[ss] = prev + 1
        
        prev += 1

    for idx in range(len(lst)):
        # flag가 true라면 최종이 아니므로 유저의 점수 더해주기
        if flag:
            user[idx] += lst[idx]
        # 해당 점수의 대회에서의 등수 result에 추가
        result.append(rate[lst[idx]])

    print(*result)


N = int(input())
# 각 유저의 점수 저장
user = [0]*N

for _ in range(3):
    score = list(map(int, input().split(" ")))
    cal_rate(score, True)

cal_rate(user, False)