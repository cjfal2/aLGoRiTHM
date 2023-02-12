from collections import deque
mystack = deque()
text = deque(input())
imsi = []

while len(text) > 0  :

    if text[0] == '<' :
        e = text.index('>')
        for _ in range(e+1):
            mystack.append(text[0])
            text.popleft()

    else :
        imsi.append(text.popleft())
        
        if len(text) == 1 :
            imsi.append(text.popleft())
            imsi = imsi[::-1]
            for i in imsi :
                mystack.append(i)

        elif text[0] == ' ' or text[0] == '<'  :
            
            imsi = imsi[::-1]
            for i in imsi :
                mystack.append(i)
            imsi = []
            if text[0] == ' ' :
                mystack.append(' ')
                text.popleft()

print(*mystack, sep='')