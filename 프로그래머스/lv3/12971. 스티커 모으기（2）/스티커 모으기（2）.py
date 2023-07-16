def solution(sticker):
    answer = 0
    length = len(sticker)
    
    if length == 1:
        return sticker[0]

    DP = [[0]*length for _ in range(2)]

    # 첫 번째 : 1번 스티커를 떼는 경우
    # 2번 스티커가 1번 스티커가 값이 작다 => 아예 안 뗌
    DP[0][0], DP[0][1] = sticker[0], max(sticker[0], sticker[1])

    # 직전 값이랑 2번째 전 스티커 + 지금 값 비교해서 더 큰 값 넣어줌
    # 1번 스티커를 뗐으므로 마지막 값은 들어가면 안 됨
    for idx in range(2, length-1):
        DP[0][idx] = max(DP[0][idx-1], DP[0][idx-2]+sticker[idx])

    # 두 번째 : 1번 스티커를 아예 안 떼는 경우
    # 2번 스티커를 뗌
    DP[1][1] = sticker[1]

    # 직전 값이랑 2번째 전 스티커 + 지금 값 비교해서 더 큰 값 넣어줌
    for idx in range(2, length):
        DP[1][idx] = max(DP[1][idx-1], DP[1][idx-2]+sticker[idx])

    answer = max(DP[0][-2], DP[1][-1])

    return answer
