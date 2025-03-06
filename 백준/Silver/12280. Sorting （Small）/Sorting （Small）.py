import sys
input = sys.stdin.read

def solve_cases(test_cases):
    results = []
    for case_num, (N, books) in enumerate(test_cases, start=1):
        odd_values = sorted([b for b in books if b % 2 != 0])  # Alex's books (ascending)
        even_values = sorted([b for b in books if b % 2 == 0], reverse=True)  # Bob's books (descending)
        
        odd_index, even_index = 0, 0
        sorted_books = []
        
        for b in books:
            if b % 2 != 0:
                sorted_books.append(odd_values[odd_index])
                odd_index += 1
            else:
                sorted_books.append(even_values[even_index])
                even_index += 1
        
        results.append(f"Case #{case_num}: " + " ".join(map(str, sorted_books)))
    
    print("\n".join(results))

def main():
    data = input().strip().split("\n")
    T = int(data[0])
    test_cases = []
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        books = list(map(int, data[index + 1].split()))
        test_cases.append((N, books))
        index += 2
    
    solve_cases(test_cases)

if __name__ == "__main__":
    main()