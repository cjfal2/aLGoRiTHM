def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    return str(num) == str(num)[::-1]


a, b = map(int, input().split())
if b > 10000000:
    b = 10000000
temp = []
for n in range(a, b+1):
    if is_palindrome(n):
        temp.append(n)
for n in temp:
    if is_prime(n):
        print(n)
print(-1)
