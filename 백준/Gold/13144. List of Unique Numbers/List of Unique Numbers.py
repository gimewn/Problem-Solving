import sys

def two_pointer():
    answer = 0
    end = 0

    for start in range(N):
        while end < N:
            # 수열의 마지막 부분이 체크되어 있으면
            if check[lst[end]]:
                # 수열의 시작 부분을 체크 해제
                check[lst[start]] = 0
                break
            else:
                # 수열의 마지막 부분 체크
                check[lst[end]] = 1
                # end ++
                end += 1
                # end - start
                # 만약 end가 3이고 start 가 0 (1 2 3)
                # 3 / 32 / 321 => 3개
                answer += end - start
    return answer

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

check = [0]*100001

print(two_pointer())