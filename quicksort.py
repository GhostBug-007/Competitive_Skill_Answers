def quicksort(list):
    l=len(list)
    if l < 2 :
        return (list)
    else:
        pivot=list[0]
        n=0
        for i in range(1,l):
            if list[i] < pivot :
                n=n+1
                list[i] , list[n] = list[n] , list[i]
        list[n] , list[0] = list[0] , list[n]
        L=quicksort(list[:n])
        R=quicksort(list[n+1:])
        L.append(list[n])
        return (L+R)
lst=list(range(10,1,-1))
lst=quicksort(lst)
print(lst)
