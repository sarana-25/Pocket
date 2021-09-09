def Main_menu():
    while True:
        print("\n")
        print("List of Function you can Implement-","1.Create","2.Display","3.Add in Beggining","4.Add at Any","5.Add in End","6.Delete in Beggining","7.Delete at Any","8.Delete in End","9.Delete a data","10.Delete Whole List","11.Display Backwards","12.Reverse","13.Exit",sep="\n")
        print("\n")
        argument=int(input("Select The function you want to Implement:"))
        print("\n")
        if(argument==13):
            break
        switch(argument,ll)
        
    
def switch(argument,ll):
    
    while True:
        if(argument==0):
            print("Enter Valid Input")
            Main_menu()
        elif(argument==1):
            ll.create()
            Main_menu()
        elif(argument==2):
            ll.display_forward()
            Main_menu()
        elif(argument==3):
            ll.insert_at_beggining(data=input("Enter data:"))
            Main_menu()
        elif(argument==4):
            ll.insert_at_middle()
            Main_menu()
        elif(argument==5):
            ll.insert_at_end(data=input("Enter data you want to add:"))
            Main_menu()
        elif(argument==6):
            ll.remove_beggining()
            Main_menu()
        elif(argument==7):
            ll.remove_any(pos=int(input("Enter the node you want to delete:")))
            Main_menu()
        elif(argument==8):
            ll.remove_last()
            Main_menu()
        elif(argument==9):
            ll.remove_by_data()
            Main_menu()
        elif(argument==10):
            ll.delete_whole()
            Main_menu()
        elif(argument==11):
            ll.display_backward()
            Main_menu()
        elif(argument==12):
            ll.reverse()
            Main_menu()
        else:
            print("Wrong choice")
            break
        break  
        
        
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class Linked_List:
    def __init__(self):
        self.head=None
    
    def create(self):
        n=int(input("Enter number of nodes:"))
        lst=[]
        for _ in range(n):
            lst.append(input("Enter data:"))
        for data in lst:
            self.insert_at_end(data)
    
    def display_forward(self):
        if self.head==None:
            print("No Item in Linked List")
            return
        itr=self.head
        items=None
        while itr:
            items=itr.data
            itr=itr.next
            print(items)
    
    def insert_at_beggining(self,data):
        node=Node(data,self.head,None)
        if self.head==None:
            self.head=node
        else:
            self.head.prev=node
            self.head=node
    
    def insert_at_middle(self):
        pos=int(input("Enter Position:"))
        if pos<0 and pos>self.length():
            print("Position out of Range")
        else:
            data=input("Enter data:")
            if pos==0:
                self.insert_at_beggining(data)
                return
            else:
                count=0
                itr=self.head
                while itr:
                    if count==pos-1:
                        node=Node(data,itr.next,itr)
                        if node.next:
                            node.next.prev=node
                        itr.next=node
                        break
                    itr=itr.next
                    count+=1
    
    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data,None,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None,itr)
        
    
    def remove_beggining(self):
        self.head=self.head.next
        self.head.prev=None
    
    def remove_any(self,pos):
        if pos<0 and pos>self.length():
            print("Position out of Range")
        else:
            count=0
            itr=self.head
            while itr:
                if count==pos-1:
                    itr.next=itr.next.next
                    if itr.next:
                        itr.next.prev=itr
                    break
                itr=itr.next
                count+=1
    
    def remove_last(self):
        pos=self.length()
        if pos==0:
            self.remove_beggining()
            return
        else:
            self.remove_any(pos)
    
    def remove_by_data(self):
        data=input("Enter the data you want to remove:")
        count=0
        itr=self.head
        while itr:
            if itr.data==data:
                self.remove_any(count)
                break
            count+=1
            itr=itr.next
    def delete_whole(self):
        while self.length() is not 0:
            self.remove_last()
    
    def display_backward(self):
        if self.head==None:
            print("No Items in Linked List")
            return
        itr=self.get_last_node()
        items=None
        while itr:
            items=itr.data
            itr=itr.prev
            print(items)
    
    def reverse(self):
        if self.head is None:
            print("No data in Linked List")
            return
        itr=self.head
        nextnode=self.head
        prevnode=None
        while itr:
           nextnode=nextnode.next
           itr.next=prevnode
           itr.prev=nextnode
           prevnode=itr
           itr=nextnode
        self.head=prevnode
   
    def get_last_node(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr
    
    def length(self):
        count=0
        itr=self.head
        while itr.next:
            count+=1
            itr=itr.next
        return count

   

if __name__=="__main__":
    ll=Linked_List()
    Main_menu()