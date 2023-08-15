import sys

def check_is_possible(word1, word2, word3):
    q = set()
    q.add((len(word1)-1, len(word2)-1, len(word3)-1))

    while q:
        n1, n2, n3 = q.pop()
        if n1 == -1 and n2 == -1 and n3 == -1:
            return 'yes'

        if word3[n3] == word1[n1]:
            q.add((n1-1, n2, n3-1))
        if word3[n3] == word2[n2]:
            q.add((n1, n2-1, n3-1))
    return 'no'

N = int(sys.stdin.readline())
for index in range(1, N+1):
    one, two, three = sys.stdin.readline().rstrip().split()
    result = check_is_possible(one, two, three)
    print(f'Data set {index}: {result}')