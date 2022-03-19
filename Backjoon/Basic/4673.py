def d(n):
    k=0
    a = list(str(n))
    for i in a:
        k += int(i)
    print(int(n) + k)

for i in range(10):
    d(i)

d(7)