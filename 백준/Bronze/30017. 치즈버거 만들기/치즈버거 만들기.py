def max_cheeseburger_size(A, B):
    patties = min(A, B + 1)
    cheese = min(B, A - 1)
    return patties + cheese

a, b = map(int, input().split())
print(max_cheeseburger_size(a, b))