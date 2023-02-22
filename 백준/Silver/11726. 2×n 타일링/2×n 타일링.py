n = int(input())

answer = [0]*(n+1)

answer[0] = 1
answer[1] = 1

for idx in range(2, n+1):
    answer[idx] = answer[idx-1]+answer[idx-2]

print(answer[n]%10007)