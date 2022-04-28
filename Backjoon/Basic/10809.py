a=input()
b=list()
for k in range(0,26):
    b.append(str(a.find(chr(97+k))))
print(" ".join(b))