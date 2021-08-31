pos=-1
def search(lst,i):
    m=0
    for m in range(len(lst)):
        if lst[m]==i:
            globals()['pos']=m
            return True
    return False


n=int(input())
lst=list()
for _ in range(n):
    lst.append(input())
i=input()
if search(lst,i):
    print("Found at ",pos+1)
else:
    print("Not Found")
