import sys

def inputdata():
    a = sys.stdin.readline().strip()
    return a

A, B = inputdata().split(" ")

Z = ["0" for i in range(int(A))]
for i in range(int(B)):
    C, D, E = inputdata().split(" ")
    for k in range(int(C) - 1, int(D)):
        Z[k] = E
print(" ".join(Z))

# seq 0. [0, 0, 0, 0, 0]
# seq 1. [3, 3, 0, 0, 0]
# seq 2. [3, 3, 4, 4, 0]
# seq 3. [1, 1, 1, 1, 0]
# seq 4. [1, 2, 1, 1, 0]