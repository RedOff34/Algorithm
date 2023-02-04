# 백준 2941

w = input()
al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

for j in range(len(al)):
    if al[j] in w:
        count -= 1 * w.count(al[j])
        
for i in range(len(w)):
    count += 1

print(count)
