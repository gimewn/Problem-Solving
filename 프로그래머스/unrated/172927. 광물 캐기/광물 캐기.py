def solution(picks, minerals):
    answer = 1e9
    total_picks = sum(picks)
    picks_name = ["dia", "iro", "sto"]
    pick = {
        "dia": {
            "diamond": 1,
            "iron": 1,
            "stone": 1
        },
        "iro": {
            "diamond": 5,
            "iron": 1,
            "stone": 1
        },
        "sto": {
            "diamond": 25,
            "iron": 5,
            "stone": 1
        }
    }

    def DFS(level, idx, tired):
        nonlocal answer
        if level == total_picks or idx > len(minerals):
            answer = min(answer, tired)

        if tired > answer:
            return

        for i in range(3):
            if picks[i] > 0:
                now = minerals[idx:idx + 5]
                picks[i] -= 1
                temp = 0
                for item in now:
                    temp += pick[picks_name[i]][item]
                DFS(level + 1, idx + 5, tired + temp)
                picks[i] += 1

    DFS(0, 0, 0)

    return answer