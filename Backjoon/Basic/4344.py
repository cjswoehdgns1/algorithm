N = int(input())
list_result=[]
for i in range(N):
    point = list(map(int, input().split()))
    person = point[0]
    z=0
    for t in range(1, person+1):
        z += point[t]
    average = z/person
    l=0
    for t in range(1, person+1):
        if point[t] > average:
            l += 1
    list_result.append("{0:.3f}%".format(l/person*100))
for z in list_result:
    print(z)