a=int(input())
b=list(map(int, input().split(" ")))
c=int(input())
z=0
for i in range(a):
    if (c == b[i]):
        z += 1
print(z)