def solution(n, results):
    answer = 0
    grade = [[None] * (n + 1) for _ in range(n + 1)]

    for winner, loser in results:
        grade[winner][loser] = True
        grade[loser][winner] = False

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if grade[i][j] != None:
                    continue
                # i가 k에게 이겼고, k도 j에게 이김 => i는 j에게 이김
                if grade[i][k] == True and grade[k][j] == True:
                    grade[i][j] = True
                # i가 k에게 졌고, k도 j에게 졌음 => i는 j에게 짐
                if grade[i][k] == False and grade[k][j] == False:
                    grade[i][j] = False

    for i in range(1, n + 1):
        lose_count = 0
        for j in range(1, n + 1):
            # 자기 자신이 아닌데 None일 경우 존재 => 순위 못 정함
            if grade[i][j] == None and i != j:
                lose_count = -1
                break
            if grade[i][j] == False:
                lose_count += 1
        if lose_count >= 0:
            print(i, lose_count)
            answer += 1

    return answer