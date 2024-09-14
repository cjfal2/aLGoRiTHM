test_case = int(input())
for tc in range(1, test_case+1):
    heads = int(input())
    arr = input()
    for command in arr:
        if command == "c":
            heads += 1
        else:
            heads -= 1
    print(f"Data Set {tc}:")
    print(heads)
    if tc != test_case:
        print()