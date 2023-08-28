def solution(cards1, cards2, goal):
    while goal:
        x = goal.pop(0)
        if cards1 and cards1[0] == x:
            cards1.pop(0)
        elif cards2 and cards2[0] == x:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"