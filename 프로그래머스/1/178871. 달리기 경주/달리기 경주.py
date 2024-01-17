def solution(players, callings):
    temp = dict()
    for idx, p in enumerate(players):
        temp[p] = idx
    
    for c in callings:
        a = temp[c]
        temp[c] -= 1
        temp[players[a-1]] += 1
        players[a], players[a-1] = players[a-1], players[a]
    
    return players