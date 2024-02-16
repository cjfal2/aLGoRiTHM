def solution(N, stations, W):
    answer = 0
    idx = 0
    position = 1

    while position <= N:
        if idx < len(stations) and position >= stations[idx] - W:
            position = stations[idx] + W + 1
            idx += 1
        else:
            position += 2 * W + 1
            answer += 1

    return answer