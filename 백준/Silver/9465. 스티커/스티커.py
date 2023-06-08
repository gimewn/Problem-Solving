import sys

def find_max():
    n = int(sys.stdin.readline())
    stickers = [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    for j in range(2, n+1):
        for i in range(2):
            if i == 0:
                new_i = i+1
            else:
                new_i = i-1
            stickers[i][j] += max(stickers[new_i][j-1], stickers[new_i][j-2])
    return max(stickers[0][-1], stickers[1][-1])

def main():

    t = int(sys.stdin.readline())
    for _ in range(t):
        print(find_max())

if __name__ == '__main__':
    main()