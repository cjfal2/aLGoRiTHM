def check(num):
    for m in range(2, int(num ** 0.5) + 1):
        if not num % m:
            return True
    return False

n = int(input())
primes = [i for i in range(2, n+1) if not check(i)]
cnt = hap = left = right = 0

while 1:
    if hap >= n:
        hap -= primes[left]
        left += 1
    elif right == len(primes):
        break
    else:
        hap += primes[right]
        right += 1
    if hap == n:
        cnt += 1

print(cnt)
