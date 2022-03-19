N=input()

K=list(map(int, input().split()))
Max_K = K[0]
Min_K = K[0]

for i in K:
    if Max_K < i:
        Max_K = i

    if Min_K > i:
        Min_K = i
print(Min_K, Max_K)