N=float(input())
K=list(map(float, input().split()))
Max_K = K[0]
t=0

for i in K:
    if Max_K < i:
        Max_K = i

for i in K:
    t += i/Max_K*100
print(float(t/N))