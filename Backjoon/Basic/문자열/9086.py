a=input()
k = []
for i in range(int(a)):
    b = input()
    k.append(list(b)[0]+list(b)[-1])
print("\n".join(k))