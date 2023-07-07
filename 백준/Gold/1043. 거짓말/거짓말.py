import sys

def visit_parties():
    global answer, know_truth
    check = [0]*M
    for _ in range(M):
        exception = 0
        plus_know_truth = set()
        for idx in range(M):
            if check[idx]:
                continue
            temp = set(parties[idx])
            flag = 0
            for person in parties[idx]:
                if person in know_truth:
                    flag = 1
                    break
            if flag:
                exception += 1
                plus_know_truth = plus_know_truth | temp
                check[idx] = 1
        if exception:
            answer -= exception
            know_truth = know_truth | plus_know_truth
        else:
            break

inputs = sys.stdin.readline

N, M = map(int, inputs().split())
know = list(map(int, inputs().split()))
know_truth = set()
parties = []

for _ in range(M):
    now_party = list(map(int, inputs().split()))
    now_party.pop(0)
    parties.append(now_party)

answer = M

if len(know) == 1:
    print(M)
else:
    know_truth = set(know[1:])
    visit_parties()
    print(answer)
