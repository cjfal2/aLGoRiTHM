for tc in range(1, int(input())+1):
    n = int(input())
    word_a = input()
    word_b = input()
    diffs = 0
    for i in range(n):
        if word_a[i] != word_b[i]:
            diffs+=1
    print(f'Case {tc}: {diffs}')