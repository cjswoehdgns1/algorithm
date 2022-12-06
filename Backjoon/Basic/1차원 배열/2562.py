from typing import Counter


a=[]
k=0
t=0
for i in range(1,10):
    n = int(input())
    a.append(n)

Max_a = a[0]

for i in a:
    k += 1
    if Max_a <= i:
        Max_a=i        
        if Max_a == i:
            t = k
        
print(Max_a)
print(t)