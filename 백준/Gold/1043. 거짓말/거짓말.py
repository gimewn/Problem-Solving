import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 사람의 수, 파티의 수
truth = list(map(int, input().split()))[1:] # 진실을 알고 있는 사람들의 번호 리스트
check = [0] * (N+1) # 진실을 알고 있는지 체크
party = [0]*M
party_check = [1]*M # 거짓말 할 수 있는 파티인지 체크

for t in truth: # 최초의 진실을 알고 있는 사람 체크
    check[t] = 1

for idx in range(M):
    party[idx] = list(map(int, input().split()))[1:] # 파티 순서대로 입력

while truth:
    truth_person = truth.pop()

    dontKnow = set() # 진실을 아직 모르는 사람들

    for idx in range(M):
        if truth_person in party[idx]: # 파티에 진실을 알고 있는 사람이 있으면
            party_check[idx] = 0 # 거짓말 할 수 없으므로 체크 해제
            dontKnow = dontKnow.union(party[idx]) # 진실을 아직 모르는 사람들에 파티원들 추가

    for person in dontKnow:
        if not check[person]: # 아직 진실을 모르면
            truth.append(person) # 진실을 알게 되었으므로 truth 리스트에 추가
            check[person] = 1 # 체크

print(sum(party_check))