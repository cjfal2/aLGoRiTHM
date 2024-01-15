def encode(a, b):
    return (a + b) % 26


def decode(c, b):
    return (c - b + 26) % 26


translated = [ord(char) - 97 for char in input()]
part_of_origin = [ord(char) - 97 for char in input()]

n, m = len(translated), len(part_of_origin)

original = [0 for _ in range(n)]
add_key = [0 for _ in range(n)]

for start in range(n - m + 1):
    for i in range(m):
        z = start + i
        original[z] = part_of_origin[i]
        add_key[z] = decode(translated[z], original[z])

    for k in range(1, m // 2 + 1):
        flag = 1
        for i in range(start, start + m - k):
            if add_key[i] != add_key[i + k]:
                flag = 0
                break

        if not flag:
            continue

        for i in range(start, start + k):
            for j in range(i % k, n, k):
                add_key[j] = add_key[i]

        for i in range(n):
            original[i] = decode(translated[i], add_key[i]) + 97

        print(''.join(map(chr, original[:n])))
        quit()
