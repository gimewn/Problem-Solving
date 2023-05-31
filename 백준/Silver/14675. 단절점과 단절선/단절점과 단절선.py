import sys
from collections import deque

def main():

    n = int(sys.stdin.readline())

    def is_cut_off(num):
        # num번 정점이 단절점인지 검사
        # num번 정점에 연결되어 있는 정점이 2개 이상 => 없앴을 때 그래프 분리됨
        if num in tree and len(tree[num]) >= 2:
            return True
        return False

    tree = {}

    for idx in range(n-1):
        a, b = map(int, sys.stdin.readline().split())

        if a in tree:
            tree[a].append([b])
        else:
            tree[a] = deque([b])
        if b in tree:
            tree[b].append([a])
        else:
            tree[b] = deque([a])


    q = int(sys.stdin.readline())

    for _ in range(q):
        t, k = map(int, sys.stdin.readline().split())
        if t == 1:
            if is_cut_off(k):
                print("yes")
            else:
                print("no")
        else:
            # 사이클이 존재하지 않으며, 모든 정점이 연결 => 모든 간선은 단절선
            print("yes")

if __name__ == "__main__":
    main()