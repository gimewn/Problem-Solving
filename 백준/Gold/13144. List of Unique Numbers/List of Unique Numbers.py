n = int(input())

nums = list(map(int, input().split()))
answer = 0
check = [0]*100001

start, end = 0, 0

while start < n and end < n:
    if not check[nums[end]]:
        check[nums[end]] = 1
        end += 1
        # 만약 end가 3이고 start가 0이라면
        # 3 / 23 / 123 ... (3개
        # end가 2이고 start가 0이면
        # 2 / 12 (2개)
        answer += end - start
    else:
        check[nums[start]] = 0
        start += 1

print(answer)