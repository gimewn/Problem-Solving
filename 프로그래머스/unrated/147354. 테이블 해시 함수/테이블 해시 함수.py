def solution(data, col, row_begin, row_end):
    answer = 0
    sum_s_i = []
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    for i in range(row_begin, row_end+1):
        temp = 0
        for num in data[i-1]:
            temp += num % i
        sum_s_i.append(temp)
    
    answer = sum_s_i[0]
    
    for idx in range(1, len(sum_s_i)):
        answer = answer ^ sum_s_i[idx]
        
    return answer