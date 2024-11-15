def solution(id_list, report, k):
    SEND = {}
    for LIST in report:
        FROM, TO = LIST.split()
        if FROM not in SEND:
            SEND[FROM] = {TO}
        else:
            SEND[FROM].add(TO)

    ARRV = {}
    for LIST in report:
        FROM, TO = LIST.split()
        if TO not in ARRV:
            ARRV[TO] = {FROM}
        else:
            ARRV[TO].add(FROM)

    ban = []
    for key, values in ARRV.items():
        if len(values) >= k:
            ban.append(key)

    answer = []
    for name in id_list:
        a = SEND.get(name)
        if a is None:
            answer.append(0)
        else:
            a = list(a)
            co = 0
            for i in a:
                if i in ban:
                    co += 1
            answer.append(co)
    return answer