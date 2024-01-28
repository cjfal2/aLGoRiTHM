for _ in range(int(input())):
    N = int(input())
    print(f"Pairs for {N}:", end=" ")
    
    answer = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            if i + j == N:
                answer.append([i, j])
    if not answer:
        print()
    else:
        num = 1
        for a in answer:
            if len(answer) == num:
                print(*a)
            else:
                print(*a, end=", ")
            num += 1