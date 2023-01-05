def solution(today, terms, privacies):
    answer = []
    
    # 오늘 날짜를 일수로 변환
    t_year, t_month, t_day = map(int, today.split("."))
    cal_today = (t_year*12*28) + (t_month*28) + t_day
    
    # 약관과 보관기관을 딕셔너리로 변환
    cal_terms = {}
    
    for t in terms:
        alp, month = t.split(" ")
        cal_terms[alp] = int(month)*28
        
    print(cal_terms)
    
    # 계산
    for idx in range(len(privacies)):
        date, category = privacies[idx].split(" ")
        p_year, p_month, p_day = map(int, date.split("."))
        cal_date = (p_year*12*28) + (p_month*28) + p_day + cal_terms[category]
        if cal_date <= cal_today:
            answer.append(idx+1)
    
    
    return answer