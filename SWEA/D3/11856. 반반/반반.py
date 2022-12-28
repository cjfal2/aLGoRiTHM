from collections import Counter

for tc in range(int(input())):
    a = Counter(list(input()))
    if len(a.keys()) == 2 and len(set(list(a.values()))) == 1:
        print(f'#{tc+1} Yes')
    else:
        print(f'#{tc+1} No')