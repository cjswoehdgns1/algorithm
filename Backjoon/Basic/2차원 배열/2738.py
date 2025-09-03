b, c = input().split(" ")

A = []
for i in range(int(b)):
    d = input().split(" ")
    A.append(d)

B = []
for i in range(int(b)):
    e = input().split(" ")
    B.append(e)

C = []
for i in range(int(b)):
    f = []
    for j in range(int(c)):
        f.append(str(int(A[i][j]) + int(B[i][j])))
    print(" ".join(f))