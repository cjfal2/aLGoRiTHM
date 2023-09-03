def next_permutation(s):
    # 1. Find the largest index k such that s[k] < s[k+1]
    k = -1
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            k = i

    if k == -1:
        return s  # s is the last permutation

    # 2. Find the largest index l such that s[k] < s[l]
    l = -1
    for i in range(k + 1, len(s)):
        if s[k] < s[i]:
            l = i

    # 3. Swap s[k] and s[l]
    s[k], s[l] = s[l], s[k]

    # 4. Reverse the sequence from s[k+1:]
    s[k + 1:] = reversed(s[k + 1:])

    return s

for tc in range(int(input())):
    b = list(input().strip())
    result = next_permutation(b)

    print("".join(result))
