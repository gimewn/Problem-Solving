def solution(n, times):
    def cal_people(limit):
        count = 0
        for t in times:
            count += limit // t
            if count >= n:
                break
        return count
        
    answer = 0
    
    times.sort()
    
    s, e = 1, max(times) * n
    
    while s <= e:
        mid = (s + e) // 2
        if cal_people(mid) >= n:
            answer = mid
            e = mid - 1
        else:
            s = mid + 1
    
    return answer