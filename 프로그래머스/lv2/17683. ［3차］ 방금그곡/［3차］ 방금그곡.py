def solution(m, musicinfos):
    def move_sharp(word):
        word = list(word)
        new_word = []
        idx = 0
        
        while idx < len(word):
            if word[idx] == '#':
                idx += 1
                continue
            if idx+1 < len(word):
                if word[idx+1] != '#':
                    new_word.append(word[idx])
                else:
                    new_word.append(word[idx]+word[idx+1])
            else:
                new_word.append(word[idx])    
            idx += 1
            
        return new_word
        
    def check_music(lst):
        ans = move_sharp(m)
        temp = ans[:]
        
        while lst and temp:
            now = lst.pop(0)
            if now == temp[0]:
                temp.pop(0)
            else:
                temp = ans[:]
                if now == temp[0]:
                    temp.pop(0)
        
        if temp:
            return False
        else:
            return True
        
    answer = '(None)'
    info_length = len(musicinfos)
    
    for i in range(info_length):
        start, end, title, music = musicinfos[i].split(",")
        shour, sminute = start.split(":")
        ehour, eminute = end.split(":")
        stime = int(shour)*60 + int(sminute)
        etime = int(ehour)*60 + int(eminute)
        
        playtime = etime-stime
        
        new_music = move_sharp(music)
        
        music_length = len(new_music)
        
        music_rot = playtime // music_length
        music_stop = playtime % music_length
        play_music = new_music*music_rot
        play_music = play_music + new_music[:music_stop]
        
        musicinfos[i] = [i, playtime, title, play_music]
    
    
    musicinfos.sort(key = lambda x: (-x[1], x[0]))
    
    for info in musicinfos:
        if check_music(info[3]):
            answer = info[2]
            break
    
    return answer