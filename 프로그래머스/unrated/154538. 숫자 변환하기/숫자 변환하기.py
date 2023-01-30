from collections import deque

def solution(x, y, n):
    answer = 0
    if x == y:
        return answer
    
    check = [0]*1000001
    q = deque()
    q.append(x)
    
    while q:
        ny = q.popleft()
        
        if 0 <= ny+n <= 1000000 and check[ny+n] == 0:
            check[ny+n] = check[ny]+1
            q.append(ny+n)
        if 0 <= ny*2 <= 1000000 and check[ny*2] == 0:
            check[ny*2] = check[ny]+1
            q.append(ny*2)
        if 0 <= ny*3 <= 1000000 and check[ny*3] == 0:
            check[ny*3] = check[ny]+1
            q.append(ny*3)
    
    if check[y] == 0:
        return -1
    else:
        return check[y]