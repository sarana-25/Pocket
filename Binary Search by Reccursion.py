
def search(lst,low,high,i):
    if high>=low:
        mid=(low+high)//2
        if lst[mid]==i:
            return mid
        elif lst[mid]>i:
            return search(lst,low,mid-1,i)
        else:
            return search(lst,mid+1,high,i)
    else:
        return -1
    

n=int(input())
lst=list()
for _ in range(n):
    lst.append(input())
lst.sort()
print(lst)
i=input()
result=search(lst,0,len(lst)-1,i)
if result!=-1:
    print("Found at ",result+1)
else:
    print("Not Found")