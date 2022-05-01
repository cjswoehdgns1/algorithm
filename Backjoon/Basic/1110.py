n=int(input())
x=n
k=0
z=101
while x!=z:
    a=0
    b=0

    if n <10:
        z=int(str(n)+str(n))
    else:
        for i in list(str(n)):
            a += int(i)
            b = i        
        if a>9:
            z=int(b+list(str(a))[1])
        else:
            z=int(b+str(a))
    k += 1
    n=z
print(k)