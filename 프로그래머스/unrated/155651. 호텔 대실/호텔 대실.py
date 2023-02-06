def solution(book_time):

    def plusTen(time):
        h, m = map(int, time.split(":"))
        m+=10
        if m>=60:
            h+=1
            m-=60
        m = str(m)
        if len(m) == 1:
            m = '0'+m
        return str(h)+":"+m

    answer = 0
    book_time.sort(reverse=True)
    rooms = [[] for _ in range(1000)]
    while book_time:
        checkIn, checkOut = book_time.pop()
        checkOut = plusTen(checkOut)
        for num in range(1000):
            if not rooms[num]:
                rooms[num].append(checkOut)
                break
            else:
                a = int((rooms[num][-1]).replace(":",""))
                b = int((checkIn).replace(":",""))
                if a <= b:
                    rooms[num].append(checkOut)
                    break
    for i in rooms:
        if i:
            answer+=1
        else:
            break
    return answer