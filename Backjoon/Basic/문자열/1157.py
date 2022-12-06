a=input()
b=list()
c=list()
for i in list(a):
    b.append(i.lower())
d = list(set(b))
for k in d:
    c.append(b.count(k))
if( c.count(max(c)) == 1 ):
    print(d[c.index(max(c))].upper())
else:
    print('?')