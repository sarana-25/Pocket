from collections import deque
stack=deque()
x=True
while x==True:
    print("Menu:","1.Push","2.Pop","3.View Stack","4.Exit",end="\n")
    n=int(input())
    if n==1:
        stack.append(input("Enter data:"))
    elif n==3:
        print(stack)
    elif n==2:
        stack.pop()
    else:
        x=False
        break
