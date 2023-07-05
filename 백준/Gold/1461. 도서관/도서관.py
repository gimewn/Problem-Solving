import sys

inputs = sys.stdin.readline

def sort_max_book(idx, max_value, plus_lst, minus_lst):
    global answer
    if idx == N-1:
        lst = plus_lst
    elif idx == 0:
        lst = minus_lst

    answer += max_value
    for _ in range(M):
        if lst:
            lst.pop(0)

def sort_books(lst):
    global answer
    while lst:
        max_this_time = -2e9
        for _ in range(M):
            if lst:
                now = lst.pop(0)
                if now < 0:
                    now = abs(now)
                max_this_time = max(max_this_time, now)
        answer += max_this_time * 2

N, M = map(int, inputs().split())
books = list(map(int, inputs().split()))
answer = 0

books.sort()

abs_max = -2e9
abs_max_idx = 0

for idx in range(N):
    if abs(books[idx]) > abs_max:
        abs_max = abs(books[idx])
        abs_max_idx = idx

plus = []
minus = []

for b in books:
    if b < 0:
        minus.append(b)
    elif b > 0:
        plus.append(b)

plus.sort(reverse=True)

sort_max_book(abs_max_idx, abs_max, plus, minus)

sort_books(plus)
sort_books(minus)

print(answer)