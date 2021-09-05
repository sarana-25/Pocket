def Main_menu():
    while True:
        print("List of Function you can Implement-","1.Create","2.Display","3.Add in Beggining","4.Add at Any","5.Add in End","6.Delete in Beggining","7.Delete at Any","8.Delete in End","9.Delete a data","10.Delete Whole List","11.Reverse","12.Exit",sep="\n")
        argument=int(input("Select The function you want to Implement:"))
        if(argument==12):
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
            ll.display()
            Main_menu()
        elif(argument==3):
            ll.insert_at_beggining()
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
            ll.reverse()
            Main_menu()
        else:
            print("Wrong choice")
            break
        break  
        
        

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_List:
    def __init__(self):
        self.head=None
    
    def create(self):
        n=int(input("Enter number of element you want to Enter:"))
        lst=[]
        for i in range(n):
            lst.append(input("Enter data:"))
        for data in lst:
            self.insert_at_end(data)
    
    def display(self):
        if self.head is None:
            print("No Data in Linked List")
            return
        itr=self.head
        items=None
        while itr:
            items=itr.data
            itr=itr.next
            print(items)
    
    def length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count


    def insert_at_beggining(self):
        data=input("Enter your data:")
        node=Node(data,self.head)
        self.head=node


    def insert_at_middle(self):
        pos=int(input("Enter position to insert data:"))
        if pos<0 and pos>self.length():
            print("Poition out of range")
        else:
            data=input("Enter your data:")
            if pos==0:
                self.insert_at_beggining()
                return
            else:
                count=0
                itr=self.head
                while itr:
                    if count==pos-1:
                        node=Node(data,itr.next)
                        itr.next=node
                        break
                    itr=itr.next
                    count+=1


    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    
    def remove_beggining(self):
        self.head=self.head.next
        
    def remove_any(self,pos):
        if pos<0 and pos>self.length():
            print("Poition out of range")
        else:
            count=0
            itr=self.head
            while itr:
                if count==pos-1:
                    itr.next=itr.next.next
                    break
                count+=1
                itr=itr.next
    
    def remove_last(self):
        pos=self.length()-1
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
            
    def reverse(self):
        if self.head is None:
            print("No data in list")
            return
        itr=self.head
        nextnode=self.head
        prevnode=None
        while itr:
            nextnode=nextnode.next
            itr.next=prevnode
            prevnode=itr
            itr=nextnode
        self.head=prevnode
if __name__ == "__main__":
    ll=Linked_List()
    Main_menu()
    