def solution(k, score):
    answer = []
    
    # 명예의 전당
    grade = []
    
    for idx in range(len(score)) :
        # k위까지 다 차지 않았을 때
        if idx < k:
            # 명예의 전당에 넣고
            grade.append(score[idx])
            # 가장 작은 값 추출
            answer.append(min(grade))
        else:
            # 명예의 전당 정렬
            grade.sort()
            # 명예의 전당에서 제일 작은 값보다 큰 값이면
            if grade[0] < score[idx]:
                # 교체
                grade[0] = score[idx]
            # 제일 작은 값 추출
            answer.append(min(grade))
            
    return answer