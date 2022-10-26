N, H = map(int, input().split())
trees = list(map(int, input().split()))

s = 0
e = max(trees)

while s <= e:
    mid = (s+e)//2
    temp = 0
    for tree in trees:
        if tree >= mid:
            temp += tree-mid
    if temp >= H:
        s = mid+1
    else:
        e = mid-1

print(e)