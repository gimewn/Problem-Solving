from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discount = [10, 20, 30, 40]
    emo_len = len(emoticons)
    # 중복 순열로 경우의 수 구하기
    pro_list = list(product(discount, repeat=len(emoticons)))
    
    for production in pro_list:
        # 이모티콘 플러스 가입자 수, 총 매출
        emoticon_plus, sales = 0, 0
        for user in users:
            limit_rate, limit_money = user[0], user[1]
            spent = 0
            for idx in range(emo_len):
                # 할인율이 유저 지정 할인율보다 크면 구매
                if production[idx] >= limit_rate:
                    spent += int(emoticons[idx] - emoticons[idx]*(production[idx]/100))
            # 총 사용한 금액이 유저 지정 총액 이상이면
            if spent >= limit_money:
                # 이모티콘 플러스 가입
                emoticon_plus += 1
            else:
                # 총액 미만이면 매출에 더함
                sales += spent
                
        # 이모티콘 플러스 가입자가 기존 최대값보다 더 많으면
        if emoticon_plus > answer[0]:
            # 이모티콘 플러스 가입자, 총 매출 모두 교체
            answer[0], answer[1] = emoticon_plus, sales
        # 이모티콘 플러스 가입자가 기존 최대값과 같고, 매출이 더 높으면
        elif emoticon_plus == answer[0] and sales > answer[1]:
            # 총 매출만 교체
            answer[1] = sales
                    
    return answer