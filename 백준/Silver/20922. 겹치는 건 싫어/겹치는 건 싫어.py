N, K = map(int, input().split())

lst = list(map(int, input().split()))

num_dict = dict()

answer = 0

start, end = 0, 0

while end < N:
    # lst[end] 와 lst[start]가 딕셔너리에 존재하지 않으면 등록
    if lst[end] not in num_dict:
        num_dict[lst[end]] = 0

    if lst[start] not in num_dict:
        num_dict[lst[start]] = 0
    
    # 만약 end인 숫자가 K개 이상이면 => start 당겨야 함
    if num_dict[lst[end]] >= K:
        # 기존 start 숫자의 등장횟수 감소시키기
        num_dict[lst[start]] -= 1
        # start 1 증가
        start += 1
    else:
        # end인 숫자가 K개 미만이면
        # end 숫자 등장 횟수 1 증가
        num_dict[lst[end]] += 1
        # answer 갱신
        answer = max(answer, end-start+1)
        # end 1 증가
        end += 1

print(answer)