a=c=int(input())
for i in range(0, int(a)):
    b=input()
    if not(list(b).__len__()==set(list(b)).__len__()):
        for k in set(list(b)):
            if (b.find(k * b.count(k)) == -1):
                c -= 1
                break
print(c)