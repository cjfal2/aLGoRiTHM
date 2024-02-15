def solution(want, number, discount):
    wishlist = {}
    ans = 0

    for i in range(len(want)):
        item = want[i]
        count = number[i]
        wishlist[item] = wishlist.get(item, 0) + count

    wishlist_len = sum(wishlist.values())

    for i in range(0, len(discount) - wishlist_len + 1):
        dislist = {}
        for j in range(i, i + wishlist_len):
            item = discount[j]
            dislist[item] = dislist.get(item, 0) + 1

        checklist = {}
        for item, count in wishlist.items():
            if item in dislist:
                if dislist[item] >= count:
                    checklist[item] = 0
                else:
                    checklist[item] = count - dislist[item]
            else:
                checklist[item] = count

        if sum(checklist.values()) == 0:
            ans += 1

    return ans
