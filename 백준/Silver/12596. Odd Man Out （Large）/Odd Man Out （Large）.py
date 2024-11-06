tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    temp = set()
    for a in list(map(int, input().split())):
        if a in temp:
            temp.remove(a)
        else:
            temp.add(a)
    answer = list(temp)[0]
    print(f"Case #{t}: {answer}")