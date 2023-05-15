# 0번 전구 => 유일하게 전 전구에 영향을 주지 않음
# 그 외 전구들 => 눌렀을 경우 앞 전구에 영향을 줌

n = int(input())
start = list(input())
end = list(input())

def switch(now, destination):
    count = 0

    for i in range(1, n):
        if now[i-1] != destination[i-1]:
            count += 1
            for j in range(i-1, i+2):
                if j >= 0 and j < n:
                    now[j] = '0' if now[j] == '1' else '1'
        if now == destination:
            return count
    return 2e9

answer1 = switch(start[:], end)

start[0] = '0' if start[0] == '1' else '1'
start[1] = '0' if start[1] == '1' else '1'

answer2 = switch(start, end)+1

answer = min(answer1, answer2)

if answer == 2e9:
    print(-1)
else:
    print(answer)