def solution(s):
    answer = len(s)
    def compare_length(length):
        nonlocal answer
        words = list(s)
        prev_word = ''
        prev_count = 0
        res = ''
        temp = ''
        flag = 1

        while words:
            if len(res) >= answer:
                return 2e9

            temp = ''
            for _ in range(length):
                if words:
                    temp += words.pop(0)
            if temp == prev_word:
                prev_count += 1
            else:
                if prev_count > 1:
                    res += f'{prev_count}{prev_word}'
                else:
                    res += prev_word
                prev_word = temp
                prev_count = 1

            if not words and temp:
                if prev_count > 1:
                    res += f'{prev_count}{prev_word}'
                else:
                    res += prev_word

        return len(res)

    for length in range(1, len(s)):
        res = compare_length(length)
        answer = min(answer, res)
    return answer