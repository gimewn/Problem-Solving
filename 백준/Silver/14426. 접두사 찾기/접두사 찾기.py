import sys

def binary_search(test_word):
    s, e = 0, N-1
    length = len(test_word)
    while s <= e:
        mid = (s + e) // 2
        if words[mid][:length] == test_word:
            return True
        if words[mid] > test_word:
            e = mid - 1
        else:
            s = mid + 1
    return False


N, M = map(int, sys.stdin.readline().split())

words = [sys.stdin.readline().rstrip() for _ in range(N)]

tests = [sys.stdin.readline().rstrip() for _ in range(M)]

count = 0

words.sort()

for test in tests:
    if binary_search(test):
        count += 1

print(count)