def is_fully_mowed(nx, ny, w, x_coords, y_coords):
    def check_coverage(coords, length):
        coords.sort()
        covered = 0.0
        for coord in coords:
            if covered < coord - w / 2:
                return False
            covered = max(covered, coord + w / 2)
        return covered >= length
    return check_coverage(x_coords, 75.0) and check_coverage(y_coords, 100.0)


def main():
    results = []
    while True:
        line = input().strip()
        nx, ny, w = line.split()
        nx, ny, w = int(nx), int(ny), float(w)

        if nx == 0 and ny == 0 and w == 0.0:
            break

        x_coords = list(map(float, input().strip().split()))
        y_coords = list(map(float, input().strip().split()))

        if is_fully_mowed(nx, ny, w, x_coords, y_coords):
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))


if __name__ == "__main__":
    main()
