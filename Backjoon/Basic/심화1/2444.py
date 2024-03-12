a=int(input())
b=list()
c=list()
for i in range(a-1, 0, -1):
    b.append(i)
b.append(0)
for i in range(1, a):
    b.append(i)

for i in b:
    t = " " * i + "*" * (2*(a-i)-1)
    c.append(t)

print(str.join("\n", c))