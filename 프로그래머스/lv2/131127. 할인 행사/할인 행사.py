def solution(want, number, discount):
    answer = 0
    d_len = len(discount)
    w_len = len(want)

    for now in range(d_len - 9):
        product = discount[now:now + 10]
        cnt = 0
        for idx in range(w_len):
            if product.count(want[idx]) == number[idx]:
                cnt += 1
        if cnt == w_len:
            answer += 1
    return answer