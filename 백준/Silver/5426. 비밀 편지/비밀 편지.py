import math

def rotate_reverse_90(matrix):
    return [list(row)[::-1] for row in list(zip(*matrix))]


for _ in range(int(input())):
    word = input()
    n = int(math.sqrt(len(word)))
    pan = [["" for _ in range(n)] for _ in range(n)]
    idx = 0
    for x in range(n):
        for y in range(n):
            pan[x][y] = word[idx]
            idx += 1
    real = rotate_reverse_90(pan)
    answer = ""
    for x in range(n-1, -1, -1):
        for y in range(n-1, -1, -1):
            answer += real[x][y]
    print(answer)
    

