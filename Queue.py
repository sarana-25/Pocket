queue=[]
x=True
while x==True:
    print("Menu","1.Push","2.Pop","3.Size","4.Print","5.Exit")
    n=int(input("Enter Choice:"))
    if n==1:
        queue.insert(0,input("Enter data:"))
    elif n==2:
        queue.pop()
    elif n==3:
        print(len(queue))
    elif n==4:
        print(queue)
    else:
        x=False
        break
