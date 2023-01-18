def solution(fees, records):
    
    def hour_min(time):
        return map(int, time.split(':'))

    def cal(minute):
        if minute <= fees[0]:
            return fees[1]
        else:
            mok, res = divmod((minute - fees[0]), fees[2])
            if res:
                mok += 1
            return mok * fees[3] + fees[1]

    cars = dict()
    for r in records:
        a,b,c = r.split()
        if b not in cars:
            h, m = hour_min(a)
            cars[b] = [h, m, 0, True]
        else:
            if c == "OUT":
                h, m = hour_min(a)
                bh, bm = cars.get(b)[:2]
                
                hh = h*60 + m
                bb = bh*60 + bm

                cars[b][2] += hh-bb
                cars[b][3] = False

            else:
                h, m = hour_min(a)
                cars[b][0], cars[b][1] = h, m
                cars[b][3] = True

    ans = sorted(cars.items())
    answer = []
    for x, y in ans:
        a,b,c,d = y
        s = 23*60+59 - (a*60+b)
        if d:
            c += s
        answer.append(cal(c))

    return answer