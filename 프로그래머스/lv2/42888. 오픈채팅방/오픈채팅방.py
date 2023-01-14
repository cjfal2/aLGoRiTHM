def solution(record):
    answer = []
    uid = dict()
    temp = []
    for r in record:
        R = r.split()
        if R[0] == "Enter":
            uid[R[1]] = R[2]
            temp.append(R[1] + "님이 들어왔습니다.")
        elif R[0] == "Leave":
            temp.append(R[1] + "님이 나갔습니다.")
        elif R[0] == "Change":
            uid[R[1]] = R[2]
    for t in temp:
        Q = t[:t.index("님")]
        answer.append(t.replace(Q, uid.get(Q)))
    
    return answer