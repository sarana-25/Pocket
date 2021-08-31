pos=-1
def search(lst,i):
    lower=0
    upper=len(lst)-1
    while lower<=upper:
        mid=(lower+upper)//2
        if lst[mid]==i:
            globals()['pos']= mid
            return True
        else:
            if lst[mid]<i:
                lower=mid+1
            else:
                upper=mid-1
    return False

n=int(input())
lst=list()
for _ in range(n):
    lst.append(input())
lst.sort()
print(lst)
i=input()
if search(lst,i):
    print("Found at ",pos+1)
else:
    print("Not Found")
