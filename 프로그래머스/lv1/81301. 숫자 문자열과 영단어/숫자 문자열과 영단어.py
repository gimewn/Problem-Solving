def solution(s):
    answer = 0
    numtoalp = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx in range(10):
        if numtoalp[idx] in s:
            s = s.replace(numtoalp[idx], str(idx))
    return int(s)