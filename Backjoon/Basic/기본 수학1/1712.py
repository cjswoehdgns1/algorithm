D=input()
A=int(D.split(" ")[0])
B=int(D.split(" ")[1])
C=int(D.split(" ")[2])
i=0
if(int(C-B) <= 0):
    print(-1)

else:
    print(int(A / (C - B) + 1))