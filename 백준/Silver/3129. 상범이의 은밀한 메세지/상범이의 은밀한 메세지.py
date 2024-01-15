def encode(a, b):
    return (a + b) % 26


def decode(c, b):
    return (c - b + 26) % 26


kod = input().strip()
n = len(kod)
kod = [ord(char) - ord('a') for char in kod]

dio = input().strip()
m = len(dio)
dio = [ord(char) - ord('a') for char in dio]

original = [0] * 1024
kljuc = [0] * 1024

for start in range(n - m + 1):
    for i in range(m):
        original[start + i] = dio[i]
        kljuc[start + i] = decode(kod[start + i], original[start + i])

    for k in range(1, m // 2 + 1):
        ok = 1
        for i in range(start, start + m - k):
            if kljuc[i] != kljuc[i + k]:
                ok = 0

        if not ok:
            continue

        for i in range(start, start + k):
            for j in range(i % k, n, k):
                kljuc[j] = kljuc[i]

        for i in range(n):
            original[i] = decode(kod[i], kljuc[i]) + ord('a')

        print(''.join(map(chr, original[:n])))
        quit()