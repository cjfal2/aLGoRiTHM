def main(word):
    if word == "#":
        quit()

    somoonja = []
    deamoonja = []
    numbers = []

    for w in word:
        if w in "0123456789":
            numbers.append(w)
        elif w.islower():
            somoonja.append(w)
        else:
            deamoonja.append(w)
    somoonja.sort()
    deamoonja.sort()
    numbers.sort()

    answer = "".join(somoonja) + "".join(deamoonja) + "".join(numbers)

    return answer



if __name__ == '__main__':
    while True:
        print(main(input()))
