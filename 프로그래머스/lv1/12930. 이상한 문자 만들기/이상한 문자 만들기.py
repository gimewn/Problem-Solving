def solution(s):
    answer = ''
    s = s.split(" ")
    
    for word in s:
        make_word = ''
        for idx in range(len(word)):
            # 짝수 인덱스는 대문자로
            if idx%2 == 0:
                make_word += word[idx].upper()
            else:
                # 홀수 인덱스는 소문자로
                make_word += word[idx].lower()
        # 만든 단어 + 공백 넣기
        answer += make_word + ' '
    # 마지막 공백 제외하고 리턴        
    return answer[:-1]