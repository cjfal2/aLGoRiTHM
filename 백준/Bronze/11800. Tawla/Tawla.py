def dice_game(T, cases):
    names = ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]
    doubles = ["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]
    
    for i, (a, b) in enumerate(cases, start=1):
        if a < b:
            a, b = b, a  # 큰 수부터 출력
        
        if a == b:
            result = doubles[a - 1]
        elif a == 6 and b == 5:
            result = "Sheesh Beesh"
        else:
            result = f"{names[a - 1]} {names[b - 1]}"
        
        print(f"Case {i}: {result}")

if __name__ == "__main__":
    T = int(input())
    cases = [tuple(map(int, input().split())) for _ in range(T)]
    dice_game(T, cases)
