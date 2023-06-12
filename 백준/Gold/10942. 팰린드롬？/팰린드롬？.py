import sys

def main():

    def check_self(length):
        for i in range(length):
            check[i][i] = 1

    def is_palindrom(lst, length):
        # 검사할 단어 개수(-1)
        for i in range(1, length):
            # 시작 인덱스
            for j in range(length - i):
                # 끝 인덱스
                k = j+i
                # 만약 시작 인덱스와 끝 인덱스의 값이 같다면
                if lst[j] == lst[k]:
                    # 길이가 2이면 팰린드롬
                    if k - j == 1:
                        check[j][k] = 1
                    # 가운데 단어들이 팰린드롬이면 팰린드롬
                    elif check[j+1][k-1]:
                        check[j][k] = 1


    N = int(sys.stdin.readline())
    nums = list(sys.stdin.readline().rstrip().split())
    M = int(sys.stdin.readline())
    check = [[0]*N for _ in range(N)]

    check_self(N)
    is_palindrom(nums, N)

    for _ in range(M):
        S, E = map(int, sys.stdin.readline().split())
        print(check[S-1][E-1])

if __name__ == '__main__':
    main()