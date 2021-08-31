def sort(lst):
    for i in range(len(lst)):
        minpos=i
        for j in range(i,len(lst)):
            if lst[j]< lst[minpos]:
                minpos=j
        temp=lst[i]
        lst[i]=lst[minpos]
        lst[minpos]=temp

n=int(input())
lst=list()
for _ in range(n):
    lst.append(input())
sort(lst)
print(lst)