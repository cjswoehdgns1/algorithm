a :int =list(input())
for i in range(a.__len__()-1):
    k = int(a[i+1]) - int(a[i])
    if ( k != int(a[i+1]) - int(a[i]) ):
        print("한수가 아닙니다.")
        break