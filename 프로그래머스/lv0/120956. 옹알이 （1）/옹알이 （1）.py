def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        stack = ''
        for alp in word:
            stack += alp
            if stack in can:
                stack = ''
        print(stack)
        if stack == '':
            answer += 1
    
    return answer