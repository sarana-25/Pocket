def sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
                

n=int(input())
lst=list()
for _ in range(n):
    lst.append(input())
sort(lst)
print(lst)