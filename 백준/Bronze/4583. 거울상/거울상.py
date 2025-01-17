def is_mirror_word(word):
    mirror_map = {
        'b': 'd', 'd': 'b',
        'p': 'q', 'q': 'p',
        'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'
    }
    mirrored = []
    for char in reversed(word):
        if char not in mirror_map:
            return "INVALID"
        mirrored.append(mirror_map[char])

    return "".join(mirrored)


def main():
    while 1:
        word = input().strip()
        if word == "#":
            break
        print(is_mirror_word(word))


if __name__ == "__main__":
    main()
