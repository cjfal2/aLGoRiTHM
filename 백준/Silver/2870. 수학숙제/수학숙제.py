import sys
input = sys.stdin.readline

nums = []
for _ in range(int(input().strip())):
    what = input().strip()
    num = ''
    for i, word in enumerate(what):
        # print("word:", word)
        if i == len(what)-1 and word in '0123456789':
            num += word
            nums.append(int(num))
            num = ''
        elif word in '0123456789':
            num += word
        else:
            if num:
                nums.append(int(num))
                num = ''
for ans in sorted(nums):
    print(ans)