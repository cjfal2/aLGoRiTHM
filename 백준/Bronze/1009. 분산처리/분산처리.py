def find_last_computer(t, cases):
    for num, power in cases:
        last_digit = num % 10
        if last_digit == 0:
            print(10)
            continue

        pattern = []
        result = last_digit

        while result not in pattern or len(pattern) == 0:
            pattern.append(result)
            result = (result * last_digit) % 10

        cycle_len = len(pattern)
        print(pattern[(power - 1) % cycle_len])

if __name__ == "__main__":
    T = int(input())
    cases = [tuple(map(int, input().split())) for _ in range(T)]
    find_last_computer(T, cases)