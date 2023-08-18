import sys

def check_alp_count(arr, dictinary, length):
    for idx in range(length):
        if arr[idx] not in dictinary:
            dictinary[arr[idx]] = 0
        dictinary[arr[idx]] += 1

def check_is_maya(dictionary):
    for w in W_count:
        if w not in dictionary or dictionary[w] != W_count[w]:
            return False
    return True

w_len, s_len = map(int, sys.stdin.readline().split())

W = sys.stdin.readline().rstrip()

S = sys.stdin.readline().rstrip()

W_count = {}
S_count = {}
answer = 0

check_alp_count(W, W_count, w_len)
check_alp_count(S, S_count, w_len-1)
start = 0

for end in range(w_len-1, s_len):
    if S[end] not in S_count:
        S_count[S[end]] = 0
    S_count[S[end]] += 1
    if check_is_maya(S_count):
        answer += 1
    S_count[S[start]] -= 1
    start += 1

print(answer)