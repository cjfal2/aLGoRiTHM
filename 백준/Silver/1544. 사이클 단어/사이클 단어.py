import sys
input = sys.stdin.readline

memo = dict()
ans = 0
for _ in range(int(input().strip())):
    word = input().strip()
    if len(memo.keys()) == 0:
        memo[word] = 1
        ans += 1
    else:
        check_word = list(word)
        flag = 1
        for keys in memo.keys():
            while 1:
                new = "".join(check_word)
                if new == keys:
                    flag = 0
                    break
                check_word.append(check_word.pop(0))
                if "".join(check_word) == word:
                    break
        if flag:
            memo[word] = 1
            ans += 1
        
                    
print(ans)

