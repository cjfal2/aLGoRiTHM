def solution(bridge_length, weight, truck_weights):
    answer = bridge_length

    dari = [0 for _ in range(bridge_length)]
    now = 0
    while truck_weights:
        answer += 1
        now -= dari.pop(0)
        if now + truck_weights[0] <= weight:
            w = truck_weights.pop(0)
            now += w
            dari.append(w)
        else:
            dari.append(0)

    return answer