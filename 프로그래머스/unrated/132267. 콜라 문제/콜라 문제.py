def solution(a, b, n):
    answer = 0
    while n >= a:
        getcoke = (n//a)*b
        empty = (n%a)
        answer += getcoke
        n = getcoke+empty
    return answer