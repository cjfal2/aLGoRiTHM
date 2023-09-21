def solution(wallpaper):
    answer = []
    N, M = len(wallpaper), len(wallpaper[0])
    
    flag = 0
    for n in range(N):
        if flag:
            break
        for m in range(M):
            if wallpaper[n][m] == "#":
                answer.append(n)
                flag = 1
                break
    
    flag = 0
    for m in range(M):
        if flag:
            break
        for n in range(N):
            if wallpaper[n][m] == "#":
                answer.append(m)
                flag = 1
                break
    
    flag = 0
    for n in range(N-1, -1, -1):
        if flag:
            break
        for m in range(M-1, -1, -1):
            if wallpaper[n][m] == "#":
                answer.append(n+1)
                flag = 1
                break
    
    flag = 0
    for m in range(M-1, -1, -1):
        if flag:
            break
        for n in range(N-1, -1, -1):
            if wallpaper[n][m] == "#":
                answer.append(m+1)
                flag = 1
                break
    print(answer)
    return answer