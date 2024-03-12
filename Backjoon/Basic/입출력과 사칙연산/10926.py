N = input()
X = input()

if int(N.split(" ")[1]) + int(X) % 60 == 60:
    print(int(N.split(" ")[0]) + int(X) // 60," ",int(N.split(" ")[1]) + int(X) % 60)