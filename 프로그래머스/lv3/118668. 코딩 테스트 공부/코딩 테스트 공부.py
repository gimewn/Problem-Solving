def solution(alp, cop, problems):
    # alp_req, cop_req, alp_rwd, cop_rwd, cost
    answer = 0
    max_alp = 0
    max_cop = 0
    # 모든 문제를 해결하기 위한 최대 알고력과 코딩력
    for pb in problems:
        max_alp = max(pb[0], max_alp)
        max_cop = max(pb[1], max_cop)
        
    # 최대 알고력과 코딩력을 넘어가면 안 됨
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    # dp 배열 생성
    dp = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]

    # 현재 알고력과 코딩력 => 시간 0으로 초기화
    dp[alp][cop] = 0

    for y in range(alp, max_alp+1):
        for x in range(cop, max_cop+1):
            if y < max_alp:
                # 알고력 1을 올리기 위해 1시간 공부
                dp[y+1][x] = min(dp[y+1][x], dp[y][x]+1)
            if x < max_cop:
                # 코딩력 1을 올리기 위해 1시간 공부
                dp[y][x+1] = min(dp[y][x+1], dp[y][x]+1)
            # 문제 하나를 선택하여 알고력과 코딩력을 높임
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if y >= alp_req and x >= cop_req:
                    # 최대 알고력과 최대 코딩력을 넘지 않아야 함
                    new_alp = min(y+alp_rwd, max_alp)
                    new_cop = min(x+cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[y][x]+cost)

    return dp[max_alp][max_cop]