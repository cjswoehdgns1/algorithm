N=int(input())
for i in range(N):
    M=list(input())
    z=0
    y=0
    for t in M:
        if t=="O":
            z+=1
        else:
            z=0
        y+=z
    print(y)