import sys

def visit_parties():
    global answer, know_truth
    # 파티에서 거짓말 들켰는지 체크
    check = [0]*M
    # M번 => 거짓말 들킨 경우 모두 확인 가능
    for _ in range(M):
        # 이번 턴에서 거짓말 들킨 파티 횟수
        exception = 0
        # 거짓말 추가로 알게 된 사람들
        plus_know_truth = set()
        for idx in range(M):
            # 이미 거짓말 들킨 파티면 continue
            if check[idx]:
                continue
            temp = set(parties[idx])
            flag = 0
            # 파티 참석자 중 거짓말 이미 알고 있는 사람이 있으면 flag 1
            for person in parties[idx]:
                if person in know_truth:
                    flag = 1
                    break
            if flag:
                exception += 1
                # 거짓말 추가로 알게 된 사람들에 이번 파티 참석자들 넣어주기
                plus_know_truth = plus_know_truth | temp
                check[idx] = 1
        # 만약 거짓말 들킨 파티가 있으면
        # answer에서 빼주고, 진실을 알고 있는 사람들에 이번에 알게 된 사람들 추가
        if exception:
            answer -= exception
            know_truth = know_truth | plus_know_truth
        else:
            # 거짓말 들킨 파티가 없으면 다 찾아준 것이므로 종료
            break

inputs = sys.stdin.readline

N, M = map(int, inputs().split())
know = list(map(int, inputs().split()))
know_truth = set()
parties = []

for _ in range(M):
    now_party = list(map(int, inputs().split()))
    # 맨 앞의 파티 참석자 수는 필요 없음
    now_party.pop(0)
    parties.append(now_party)

answer = M

# 진실을 알고 있는 사람이 0명이면 바로 파티 수 출력
if len(know) == 1:
    print(M)
else:
    know_truth = set(know[1:])
    visit_parties()
    print(answer)
