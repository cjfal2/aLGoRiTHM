def stars(n=3):
    if n > N:
        return
    print(" "*(N-(n-2)), "*", sep="")
    print(" "*(N-(n-1)), "*", " ", "*", sep="")
    print(" "*(N-(n-0)), "*"*5, sep="")
    stars(n+3)



N = int(input())
stars()