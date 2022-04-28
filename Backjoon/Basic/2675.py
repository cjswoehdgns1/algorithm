T = int(input())
for i in range(0, T):
    b=list()
    S=input()
    k = S.split()
    for y in list(k[1]):
        for z in range(0, int(k[0])):
            b.append(y)
    print("".join(b))