# n일 뒤의 높이는 몇일까?
# n * UP - (n-1) * DN < HT
# n ( UP - DN ) < HT - DN
# n < ( HT - DN ) / ( UP - DN )

import time

a=input().split(" ")
U = int(a[0])
D = int(a[1])
H = int(a[2])
start = time.time()

# binary search

def binary_search(U, D, H):
    # data.sort()
    start = 0
    end = 1000000000
    cnt=0
    #stime = time.time()
    while start <= end:
        mid = (start + end) // 2

        if mid == ( H - D ) / ( U - D ):
            cnt+=1
            #etime = time.time() - stime
            #print(f"{etime:.1f} sec")
            #print(cnt)
            return mid
        elif mid < ( H - D ) // ( U - D ):
            cnt+=1
            start = mid + 1
        else:
            cnt+=1
            end = mid -1

    while (mid * U - (mid - 1) * D < H):
        mid+=1
    return mid
print(binary_search(U, D, H))
# linear search
# k=0
# z=1
# while ( H > k ):
#     k+=U
#     if ( H > k ):
#         z+=1
#         k-=D
#     else:
#         end = time.time() - start
#         print(f"{end:.1f} sec")
#         break
# print(int(z))