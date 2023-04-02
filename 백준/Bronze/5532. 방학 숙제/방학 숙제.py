L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

max_ = 0
if A%C:
    max_ = max(max_, A//C + 1 )
else:
    max_ = max(max_, A//C )
if B%D:
    max_ = max(max_, B//D + 1 )
else:
    max_ = max(max_, B//D )

print(L-max_)