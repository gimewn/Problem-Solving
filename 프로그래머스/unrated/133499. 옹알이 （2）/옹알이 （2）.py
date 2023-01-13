def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    for babble in babbling:
        stack = ''
        past = ''
        # babble의 단어 하나하나 스택에 더해주기
        for word in babble:
            stack += word
            # stack이 발음할 수 있는 단어에 속하고, 연속해서 같은 발음이 아니라면
            if stack in can and stack != past:
                # 발음 기록
                past = stack
                # stack 비우기
                stack = ''
        # stack에 남은 단어가 없으면 = 모두 발음 가능한 단어
        if len(stack) == 0:
            answer += 1
    return answer