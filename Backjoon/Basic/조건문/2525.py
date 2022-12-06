a=input()
b=int(input())
c=a.split()
d=int(c[0]) + b//60
e=int(c[1]) + b%60
if ( e > 59):
    d += 1
    e -= 60
if ( d > 23):
    d -= 24
print(d, e)