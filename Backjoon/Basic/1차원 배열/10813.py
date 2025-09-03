import sys

def inputdata():
    a = sys.stdin.readline().strip()
    return a

A, B = inputdata().split(" ")

Z = [str(i) for i in range(1, int(A)+1)]
for i in range(int(B)):
    C, D = inputdata().split(" ")
    a = Z[int(C)-1]
    b = Z[int(D)-1]
    Z[int(C)-1] = b
    Z[int(D)-1] = a
print(" ".join(Z))

# seq 0. [1, 2, 3, 4, 5]
# seq 1. [2, 1, 3, 4, 5]
# seq 2. [2, 1, 4, 3, 5]
# seq 3. [3, 1, 4, 2, 5]
# seq 4. [3, 1, 4, 2, 5]