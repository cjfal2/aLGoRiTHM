N = int(input())
word = input()
small_rainbow = {'r', 'o', 'y', 'g', 'b', 'i', 'v'}
big_rainbow = {'R', 'O', 'Y', 'G', 'B', 'I', 'V'}
for w in word:
    if w in small_rainbow:
        small_rainbow.remove(w)
    elif w in big_rainbow:
        big_rainbow.remove(w)

if len(small_rainbow) == 0 and len(big_rainbow) == 0:
    print('YeS')
elif len(small_rainbow) == 0:
    print('yes')
elif len(big_rainbow) == 0:
    print('YES')
else:
    print('NO!')