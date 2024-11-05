def solution(keyinput, board):
    directions = {
        "down": (0, -1),
        "up": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }
    N, M = board[0], board[1]
    sx, sy = N//2, M//2

    x, y = 0, 0
    for command in keyinput:
        dx, dy = directions[command]
        nx, ny = x + dx, y + dy
        if sx >= nx >= -sx and sy >= ny >= -sy:
            x, y = nx, ny
    # x += sx
    # y += sy
    
    return [x, y]