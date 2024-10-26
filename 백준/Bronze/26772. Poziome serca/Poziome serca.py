a = [
    " @@@   @@@ ",
    "@   @ @   @",
    "@    @    @",
    "@         @",
    " @       @ ",
    "  @     @  ",
    "   @   @   ",
    "    @ @    ",
    "     @     "
]

n = int(input())
for i in range(9):
    for j in range(n):
        print(a[i], end = " " if j < n-1 else "")
    print()