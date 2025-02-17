while 1:
    money, how, many = input().split()
    if money == many == "0" and how == "W":
        break
    money = int(money)
    many = int(many)
    print(money + many if how == "D" else "Not allowed" if money - many < -200 else money - many)