import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

for i in range(0,10):
    print(list(str(A * B * C)).count(str(i)))