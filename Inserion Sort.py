def insertion_sort(lst,low,high):
    for i in range(1,len(lst)):
        temp=lst[i]
        j=i-1
        while j>=0 and lst[j]>temp:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=temp

    

n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
insertion_sort(lst,0,len(lst)-1)
print(lst)