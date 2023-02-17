def solution(cards1, cards2, goal):
    answer = 0
    index01, index02 = 0, 0
    for word in goal:
        if index01 < len(cards1) and word == cards1[index01]:
            index01 += 1
            answer += 1
        elif index02 < len(cards2) and word == cards2[index02]:
            index02 += 1
            answer += 1
    
    if answer == len(goal):
        return "Yes"
    else:
        return "No"