def main(n, cows):
    stack = []
    for c in cows:
        if c == ">":
            stack.append(c)
        else:
            if stack and stack[-1] == ">":
                stack.pop()
            else:
                stack.append(c)
    return "illegal" if stack else "legal"



if __name__ == "__main__":
    for _ in range(int(input())):
        temp = input().split()
        a, b =  int(temp[0]), temp[1]
        print(main(a, b))