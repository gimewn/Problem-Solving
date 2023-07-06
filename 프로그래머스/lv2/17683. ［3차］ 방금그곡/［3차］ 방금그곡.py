def solution(m, musicinfos):
    # 샵인 음 처리해주기
    def move_sharp(word):
        word = list(word)
        new_word = []
        idx = 0
        
        while idx < len(word):
            # 만약 현재 원소가 #이면 idx+1하고 continue
            if word[idx] == '#':
                idx += 1
                continue
            # 다음 원소가 #이면 현재 원소+#을 new_word에 넣어줌
            if idx+1 < len(word):
                if word[idx+1] != '#':
                    new_word.append(word[idx])
                else:
                    new_word.append(word[idx]+word[idx+1])
            else:
                # 다음 원소가 #이 아니면 현재 원소를 new_word에 넣어줌
                new_word.append(word[idx])
            idx += 1
            
        return new_word
    
    # 해당 악보 안에 찾는 음이 있는지 확인
    def check_music(lst):
        temp = sharp_m[:]
        
        while lst and temp:
            # 악보 가장 앞에 있는 거 빼주기
            now = lst.pop(0)
            # 만약 temp의 첫번째와 같다면 찾는 음의 첫번째와 같은 것이므로
            if now == temp[0]:
                # 찾는 음의 첫번째 제거
                temp.pop(0)
            else:
                # 같지 않으면 temp 초기화
                temp = sharp_m[:]
                # temp의 첫음이 현재 음과 같으면 temp의 첫 음 제거
                if now == temp[0]:
                    temp.pop(0)
        # temp가 아직 남아 있으면 => 악보 안에 없는 것
        if temp:
            return False
        # temp가 비었으면 => 악보 안에 있는 것
        else:
            return True
        
    answer = '(None)'
    info_length = len(musicinfos)
    # 찾으려는 음 분리해주기 (# 처리)
    sharp_m = move_sharp(m)
    
    for i in range(info_length):
        start, end, title, music = musicinfos[i].split(",")
        # 재생 시간 계산
        shour, sminute = start.split(":")
        ehour, eminute = end.split(":")
        stime = int(shour)*60 + int(sminute)
        etime = int(ehour)*60 + int(eminute)
        
        playtime = etime-stime
        
        # 악보의 # 처리
        new_music = move_sharp(music)
        
        music_length = len(new_music)
        
        # 재생 시간동안 재생된 악보 계산
        music_rot = playtime // music_length
        music_stop = playtime % music_length
        play_music = new_music*music_rot
        play_music = play_music + new_music[:music_stop]
        
        musicinfos[i] = [i, playtime, title, play_music]
    
    # 재생된 시간 (내림차순), 등장 순서(인덱스, 오름차순) 정렬
    musicinfos.sort(key = lambda x: (-x[1], x[0]))
    
    for info in musicinfos:
        # 만약 해당 곡의 재생된 악보 안에 찾는 음이 있으면
        if check_music(info[3]):
            # 답 갱신 => 이미 조건대로 정렬되었으므로 그만 찾아도 됨
            answer = info[2]
            break
    
    return answer
