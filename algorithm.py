# 백준 1157
X = input()
c = [0 for i in range(26)]
for i in range(len(X)):
    if 90 < ord(X[i]):
        a = ord(X[i])-32
        c[a-65] += 1
    else:
        a = ord(X[i])
        c[a-65] += 1
a = c.index(max(c))
c.sort()
if c[24] == c[25]:
    print('?')
else:
    print(chr(65+a))
