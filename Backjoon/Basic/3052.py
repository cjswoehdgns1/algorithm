import sys
t=0

list_test = []
list_result = []

for i in range(1, 11):
    N = int(sys.stdin.readline().strip())
    list_test.append(N)

for i in list_test:    
    list_result.append(i % 42)

for i in range(0, 42):
    if list_result.count(i) != 0:
        t += 1

print(t)