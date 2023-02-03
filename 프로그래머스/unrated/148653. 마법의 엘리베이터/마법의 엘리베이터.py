def solution(storey):
    answer = 0
    
    while storey:
        now = storey % 10
        storey //= 10
        
        # 맨 끝 수가 5보다 작으면 - 버튼 누르기
        if now < 5:
            answer += now
        # 맨 끝 수가 5와 같으면
        elif now == 5:
            next = storey % 10
            # 다음 수가 5 이상일 경우 -> + 버튼 누르고, 그 다음 끝 수에 +1
            # 다음 수가 5 미만일 경우 -> - 버튼 누르기
            if next >= 5:
                storey += 1
            answer += 5
        # 맨 끝 수가 5보다 크면 + 버튼 누르고, 그 다음 끝 수에 +1
        else:
            answer += 10 - now
            storey += 1
    
    return answer