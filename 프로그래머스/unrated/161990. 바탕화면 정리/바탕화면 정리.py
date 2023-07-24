def solution(wallpaper):
    answer = []
    files = []
    
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                files.append((x, y))
    
    min_x = min(files, key=lambda x : x[0])[0]
    min_y = min(files, key=lambda x : x[1])[1]
    max_x = max(files, key=lambda x : x[0])[0]
    max_y = max(files, key=lambda x : x[1])[1]
                
    return [min_x, min_y, max_x+1, max_y+1]