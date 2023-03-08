def solution(genres, plays):
    answer = []
    info = dict()
    N = len(genres)
    
    for idx in range(N):
        gen = genres[idx]
        
        if gen not in info:
            info[gen] = [plays[idx], [(plays[idx], idx)]]
        else:
            info[gen][0] += plays[idx]
            info[gen][1].append((plays[idx], idx))
    
    
    for x, arr in sorted(info.values(), reverse=True):
        arr.sort(reverse=True)
        if len(arr) == 1:
            answer.append(arr[0][1])
        else:
            a = arr[0]
            b = arr[1]
            if a[0] == b[0] and b[1] < a[1]:
                a, b = b, a
            answer.append(a[1])
            answer.append(b[1])
    
    return answer