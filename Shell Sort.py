def shell_sort(lst):
    gap=len(lst)//2
    while gap>0:
        for i in range(gap,len(lst)):
            anchor=lst[i]
            j=i
            while j>=gap and lst[j-gap]>anchor:
                lst[j]=lst[j-gap]
                j-=gap
            lst[j]=anchor
        gap=gap//2
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
shell_sort(lst)
print(lst)