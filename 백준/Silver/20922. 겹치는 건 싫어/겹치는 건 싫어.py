import sys

def two_pointer():
    answer = 0
    end = 0

    check = [0] * 100001

    for start in range(N):
        while end < N:
            if check[lst[end]] >= K:
                check[lst[start]] -= 1
                break

            else:
                check[lst[end]] += 1
                end += 1
                answer = max(answer, end - start)

    return answer

N, K = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

print(two_pointer())