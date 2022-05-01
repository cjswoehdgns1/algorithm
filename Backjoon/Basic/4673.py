c=[]
def d(n):
    k=0
    a = list(str(n))
    for i in a:
        k += int(i)
    c.append(int(n) + k)
    if int(n) + k > 10000:

        return c
    return d(int(n) + k)


f =set(range(1, 10000)) - set( d(1) )

print(set(range(1, 10000)) - set( d(7) ))