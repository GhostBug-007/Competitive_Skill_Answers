# def quicksort(list):
#     l=len(list)
#     if l < 2 :
#         return (list)
#     else:
#         pivot=list[0]
#         n=0
#         for i in range(1,l):
#             if list[i] < pivot :
#                 n=n+1
#                 list[i] , list[n] = list[n] , list[i]
#         list[n] , list[0] = list[0] , list[n]
#         L=quicksort(list[:n])
#         R=quicksort(list[n+1:])
#         L.append(list[n])
#         return (L+R)
# import sys
# sys.setrecursionlimit(10000)
# import random   
T=int(input())
# result=[]
for case in range(T):
    N,K=map(int,input().split())
    # K-=1
    array=list(map(int,input().split()))
    # print(array)
    # random.shuffle(array)
    # print(array)
    # array=quicksort(array)
    array.sort()
    # print(array)
    # array.reverse()
    while(1):
        try:
            if(array[-K] != array[-(K+1)]): break
            K=K+1
        except:
            break
    print(K)