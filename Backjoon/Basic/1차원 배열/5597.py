a=[]
for i in range(28):
    a.append(int(input()))
b=list(range(1, 31))
for k in a:
    b.remove(k)
for j in b:
    print(j)