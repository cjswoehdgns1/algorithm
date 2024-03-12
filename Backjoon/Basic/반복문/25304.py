a=int(input())
b=int(input())
d=0
for i in range(b):
    c=input().split(" ")
    d+=int(c[0])*int(c[1])
if(a==d):
    print("Yes")
else:
    print("No")