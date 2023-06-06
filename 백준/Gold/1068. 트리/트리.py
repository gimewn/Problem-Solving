import sys

def del_child(node):
    # parents_node가 parents에 있음 => 리프 노드 아님
    if node in parents:
        # 연결되어 있는 노드들 지우기
        for children in parents[node]:
            del_child(children)
        # 연결되어 있는 노드를 모두 지웠으면 자기도 지우기
        del parents[node]

    if node in child:
        del child[node]

    return

n = int(sys.stdin.readline())

# 특정 자식 노드의 부모 노드
child = {}
# 특정 노드에 연결되어 있는 자식 노드들
parents = {}
answer = 0


parents_node = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())

for idx in range(n):
    # 루트면 컨티뉴
    if parents_node[idx] == -1:
        continue

    if parents_node[idx] not in parents:
        parents[parents_node[idx]] = []

    if idx not in child:
        child[idx] = 0
    
    # 부모 노드에 자식 노드 넣어주기
    parents[parents_node[idx]].append(idx)
    # 자식 노드에 부모 노드 넣어주기
    child[idx] = parents_node[idx]

# remove_node에 부모가 있으면
if remove_node in child:
    # 부모 노드의 자식 노드 목록에서 remove_node 제거
    parents[child[remove_node]].remove(remove_node)
    # 자식 노드 딕셔너리에서 remove_node 제거
    del child[remove_node]

# 연결되어 있는 자식 지우기
del_child(remove_node)

# 자식 노드가 아무것도 안 남았으면 부모 노드의 개수 출력
if not child:
    print(len(parents))
else:
    for c in child:
        # c가 부모 노드 목록에 없거나, 연결된 자식 노드가 없으면
        if c not in parents or not len(parents[c]):
            answer += 1
    print(answer)