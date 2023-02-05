def solution(s, skip, index):
    answer = ''
    # skip 여부 기록 리스트
    check = [1] * ((ord('z') - ord('a')) + 1)
    last = len(check)
    
    # skip 알파벳 기록
    for skipAlp in skip:
        check[ord(skipAlp) - ord('a')] = 0
    
    for alp in s:
        idx = 1
        # skip에 없는 알파벳 건너 뛴 횟수
        passIdx = 0
        change = ''
        alpOrd = ord(alp) - ord('a')
        # index 이상 건너뛰면 종료
        while passIdx < index:
            checkOrd = alpOrd + idx
            # 현재 위치가 리스트 벗어나면 (z를 넘어가면)
            if checkOrd >= last:
                # 다시 a로 복귀
                checkOrd %= last
            
            # 건너 뛸 수 있으면 (skip에 해당 알파벳 없으면)
            if check[checkOrd]:
                # pass
                passIdx += 1
                # pass한 횟수가 인덱스와 같으면 => answer에 알파벳 더하기
                if passIdx == index:
                    change = chr(checkOrd + ord('a'))
            # 다음 알파벳으로
            idx += 1
            
        answer += change
        
    return answer