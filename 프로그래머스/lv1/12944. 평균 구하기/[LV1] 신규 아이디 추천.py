new_id = "abcdefghijklmn.p"


def solution(new_id):
    new_id1 = new_id.lower()

    new_id2 = []
    check = '1234567890qwertyuioopasdfghjklzxcvbnm-_.'
    for i in new_id1:
        if i in check:
            new_id2.append(i)

    new_id3 = []
    while new_id2:
        new_id3.append(new_id2.pop(0))
        if len(new_id3) > 1:
            if new_id3[-2] == new_id3[-1] == '.':
                new_id3.pop()
    if new_id3:
        if '.' == new_id3[0]:
            new_id3 = new_id3[1:]
    if new_id3:
        if '.' == new_id3[-1]:
            new_id3 = new_id3[:-1]

    if not new_id3:
        new_id3.append('a')

    if len(new_id3) > 15:
        new_id3 = new_id3[:15]
        if '.' == new_id3[0]:
            new_id3 = new_id3[1:]
        if '.' == new_id3[-1]:
            new_id3 = new_id3[:-1]

    if len(new_id3) < 3:
        a = new_id3[-1]
        while len(new_id3) != 3:
            new_id3.append(a)

    answer = ''.join(new_id3)
    return answer


print(solution(new_id))
