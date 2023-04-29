import sys

N = int(sys.stdin.readline())

S = set()

for _ in range(N):
    temp = sys.stdin.readline().split()
    command = temp[0]
    if len(temp) > 1:
        num = int(temp[1])

    if command == 'add':
        S.add(num)
    elif command == 'remove':
        S.add(num)
        S.remove(num)
    elif command == 'check':
        temp_length = len(S)
        S.add(num)
        if len(S) > temp_length:
            print(0)
            S.remove(num)
        else:
            print(1)
    elif command == 'toggle':
        temp_length = len(S)
        S.add(num)
        if len(S) == temp_length:
            S.remove(num)
    elif command == 'all':
        S = set(x for x in range(1, 21))
    elif command == 'empty':
        S.clear()