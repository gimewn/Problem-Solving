import sys

def find_partner(lst):
    global answer
    if lst:
        while len(lst) >= 2:
            one = lst.pop(0)
            two = lst.pop(0)

            answer += max(one * two, one + two)

inputs = sys.stdin.readline

N = int(inputs())

plus = []
minus = []

answer = 0

zero = 0

for _ in range(N):
    num = int(inputs())
    if N == 1:
        print(num)
        exit()
    if num > 0:
        plus.append(num)
    elif num == 0:
        plus.append(num)
        zero += 1
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()

if len(minus) % 2 == 1 and zero:
    zero -= 1
    plus.pop()
    minus.pop()

if plus:
    find_partner(plus)
if minus:
    find_partner(minus)
if plus or minus:
    left = plus+minus
    find_partner(left)

    if left:
        answer += left[0]

print(answer)