def quick_sort(lst,low,high):
    while low<=high:
        if len(lst)==1:
            return lst
        else:
            partition_index=partition(lst,low,high)
            quick_sort(lst,low,partition_index-1)
            quick_sort(lst,partition_index+1,high)
            return lst
    
def partition(lst,low,end):
    pivot_index=low
    pivot=lst[pivot_index]
    start=low+1
    while(start<=end):
        while start<=len(lst)-1 and lst[start]<=pivot:
            start+=1
        while end>=low and lst[end]>pivot:
            end-=1
        if start<end:
            swap(lst,start,end)
    swap(lst,pivot_index,end)
    return end

def swap(lst,a,b):
    lst[a],lst[b]=lst[b],lst[a]
    

n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
quick_sort(lst,0,len(lst)-1)
print(lst)