a=input()
b=a.split()

if(set(b).__len__() == 1):
    print(10000 + int(b[0])*1000)
elif(set(b).__len__() == 2):
    if b.count(list(set(b))[0]) == 2:
        print(1000 + int(list(set(b))[0])*100)
    else:
        print(1000 + int(list(set(b))[1])*100)
else:
    print(int(max(b))*100)