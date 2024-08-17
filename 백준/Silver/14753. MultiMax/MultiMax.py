def max_product(n, cards):
    cards.sort()

    max1 = cards[-1] * cards[-2] * cards[-3]
    max2 = cards[-1] * cards[0] * cards[1]
    max3 = cards[-1] * cards[-2]
    max4 = cards[0] * cards[1]

    return max(max1, max2, max3, max4)

n = int(input())
cards = list(map(int, input().split()))

print(max_product(n, cards))
