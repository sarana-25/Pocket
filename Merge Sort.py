def merge_sort(lst):
    if len(lst)<=1:
        return
    mid=(len(lst))//2
    left=lst[:mid]
    right=lst[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,lst)

def merge(left,right,lst):
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            lst[k]=left[i]
            i+=1
        else:
            lst[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        lst[k]=left[i]
        i+=1
        k+=1
    while j<len(left):
        lst[k]=right[j]
        j+=1
        k+=1
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
merge_sort(lst)
print(lst)