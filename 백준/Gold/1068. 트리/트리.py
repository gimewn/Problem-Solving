import sys

def del_child(node):
    # parents_node가 parents에 있음 => 리프 노드 아님
    if node in parents:
        # 연결되어 있는 노드들 지우기
        for children in parents[node]:
            del_child(children)
        del parents[node]

    if node in child:
        del child[node]

    return

n = int(sys.stdin.readline())

child = {}
parents = {}
answer = 0

parents_node = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())
root = 0

for idx in range(n):
    if parents_node[idx] == -1:
        root = idx
        continue

    if parents_node[idx] not in parents:
        parents[parents_node[idx]] = []

    if idx not in child:
        child[idx] = 0

    parents[parents_node[idx]].append(idx)
    child[idx] = parents_node[idx]

if remove_node in child:
    parents[child[remove_node]].remove(remove_node)
    del child[remove_node]

# 연결되어 있는 자식 지우기
del_child(remove_node)

if not child:
    print(len(parents))
else:
    for c in child:
        if c not in parents or not len(parents[c]):
            answer += 1
    print(answer)