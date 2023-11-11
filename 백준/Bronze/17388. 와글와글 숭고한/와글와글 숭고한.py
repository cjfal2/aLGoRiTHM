answer = ""
MIN = 101
hap = 0
arr = list(map(int, input().split()))
for idx, w in enumerate(["Soongsil", "Korea", "Hanyang"]):
    hap += arr[idx]
    if MIN > arr[idx]:
        MIN = arr[idx]
        answer = w
print("OK" if hap >= 100 else answer)