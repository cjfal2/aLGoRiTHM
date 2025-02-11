import sys

input = sys.stdin.readline


def is_semi_magick(square, S):
    n = len(square)
    for row in square:
        if sum(row) != S:
            return False
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != S:
            return False
    return True


def is_weakly_magick(square, S):
    n = len(square)
    if not is_semi_magick(square, S):
        return False
    if sum(square[i][i] for i in range(n)) != S:
        return False
    if sum(square[i][n - 1 - i] for i in range(n)) != S:
        return False
    return True


def is_strongly_magick(square, S):
    n = len(square)
    if not is_weakly_magick(square, S):
        return False
    numbers = [num for row in square for num in row]
    return len(set(numbers)) == n * n


def is_magically_magick(square, S):
    n = len(square)
    if not is_strongly_magick(square, S):
        return False
    numbers = sorted([num for row in square for num in row])
    return numbers == list(range(min(numbers), min(numbers) + n * n))


squares = []

while 1:
    n = int(input().strip())
    if n == 0:
        break
    square = [list(map(int, input().strip().split())) for _ in range(n)]
    squares.append(square)

for idx, square in enumerate(squares, 1):
    S = sum(row[0] for row in square)
    if is_magically_magick(square, S):
        result = "Magically-Magick Square"
    elif is_strongly_magick(square, S):
        result = "Strongly-Magick Square"
    elif is_weakly_magick(square, S):
        result = "Weakly-Magick Square"
    elif is_semi_magick(square, S):
        result = "Semi-Magick Square"
    else:
        result = "Not a Magick Square"
    print(f"Square {idx}: {result}")
