N = int(input())
seats = [0] + list(map(int, input().split()))
who_move = 1
swaps = 0

while 1:
    if seats[1] == 0:
        break
    # who_move를 who_move에 넣고 who_move를 그자리에 있던 애로 바꾼다.
    if seats[who_move]:
        new_who_move = seats[who_move]
        seats[who_move] = who_move
        who_move = new_who_move
    else:
        break
    swaps += 1


print(swaps)