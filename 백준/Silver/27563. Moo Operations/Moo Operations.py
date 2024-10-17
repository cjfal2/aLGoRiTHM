for _ in range(int(input())):
    word = input()
    if "MOO" in word:
        print(len(word)-3)
    elif "MOM" in word:
        print(len(word)-2)
    elif "OOO" in word:
        print(len(word)-2)
    elif "OOM" in word:
        print(len(word)-1)
    else:
        print(-1)