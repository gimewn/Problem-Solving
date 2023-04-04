def solution(plans):
    answer = []
    wait = []

    plans.sort(key=lambda x: x[1])

    for p in plans:
        sub, start_time, play = p
        # hh:mm => 분 단위로 바꿔주기
        hour, minute = map(int, start_time.split(":"))
        cal_time = hour * 60 + minute
        p[1] = cal_time
        p[2] = int(p[2])

    for idx in range(len(plans)):
        # 종료 시간 구하기
        total = plans[idx][1] + plans[idx][2]
        if idx == len(plans)-1:
            answer.append(plans[idx][0])
        else:
            # 다음 시작 시간
            next_value = plans[idx + 1][1]
            # 종료 시간 > 다음 시작 시간 => 기다려야 함
            if total > next_value:
                plans[idx][2] -= next_value - plans[idx][1]
                # wait에 추가
                wait.append([plans[idx][0], plans[idx][2]])
                # play_time 줄여주기
            else:
                # 끝났으므로 answer에 추가
                answer.append(plans[idx][0])
                # 다음 시작 시간까지 남은 여유시간
                left = next_value - total
                # 기다리고 있는 과제가 있고, 다음 시작 시간까지 1분 이상 남았다면
                if wait and left > 0:
                    temp = wait[:]
                    for idx in range(len(temp)-1, -1, -1):
                        title, playtime = temp[idx]
                        if playtime < left:
                            wait.pop(idx)
                            answer.append(title)
                            left -= playtime
                        elif playtime == left:
                            wait.pop(idx)
                            answer.append(title)
                            break
                        else:
                            wait[idx][1] -= left
                            break

    # 남은 대기 중인 과제들 => 뒤에서부터 answer에 넣어주기(가장 최근에 들어옴 => 먼저 나감)
    for item in wait[::-1]:
        answer.append(item[0])

    return answer