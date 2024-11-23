def solve(A, B, C):
    if A == 0 or B == 0 or C == 0:
        return "S"
    if A + B == 0 or A + C == 0 or B + C == 0:
        return "S"
    if A - B == 0 or A - C == 0 or B - C == 0:
        return "S"
    if B - A == 0 or C - A == 0 or C - B == 0:
        return "S"
    if A + B + C == 0 or A + B - C == 0 or A - B + C == 0 or A - B - C == 0:
        return "S"
    if -A + B + C == 0 or -A + B - C == 0 or -A - B + C == 0:
        return "S"
    return "N"


A, B, C = map(int, input().split())
print(solve(A, B, C))
