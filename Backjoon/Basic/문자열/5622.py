s=input()
a={}
b=[3, 3, 3, 3, 3, 4, 3, 4]
c=3
k=0
h=0
for i in b:
    for z in range(0, i):
        a[chr(65+z+k)] = c
    k += i
    c += 1
for p in list(s):
    h += a[p]
print(h)