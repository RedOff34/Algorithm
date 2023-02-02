# 백준 1065
X = input()

count = 0

if len(X) <= 2:
    count = X
    
elif len(X) >= 3:
    count += 99
    for i in range(100, int(X)+1):
        a = int(str(i)[0]) - int(str(i)[1])
        b = int(str(i)[1]) - int(str(i)[2])
        if a == b:
            count +=1
print(count)