from collections import defaultdict

def solution(elements):
    dict = defaultdict(int)
    answer = 0
    length = len(elements)

    for limit in range(1, length+1):
        new_elements = elements + elements[:limit-1]
        for num in range(len(new_elements)-limit+1):
            sums = sum(new_elements[num:num+limit])
            if sums not in dict:
                dict[sums] += 1
                answer += 1

    return answer