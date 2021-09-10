def Main_menu():
    while True:
        print("List of Function you can Implement-","1.Get","2.Set","3.Delete","4.Print","5.Exit",sep="\n")
        argument=int(input("Select The function you want to Implement:"))
        if(argument==5):
           return False
        switch(argument,Hash_Table)

def switch(argument,Hash_Table):
    while True:
        if(argument==0):
            print("Enter Valid Input")
            Main_menu()
        elif(argument==1):
            Hash_Table.get_value(key=input("Enter key you want to get:"))
            Main_menu()
        elif(argument==2):
            Hash_Table.set_values(key=input("Enter key:"),value=input("Enter value:"))
            Main_menu()
        elif(argument==3):
            Hash_Table.del_value(key=input("Enter key you want to delete:"))
            Main_menu()
        elif(argument==4):
            print(Hash_Table.hash_table)
            Main_menu()
        elif(argument==5):
            pass
        else:
            print("Wrong Choice")
        
        
        
class HashTable:
    #Creatig empty arrays
    def __init__(self,size):
        self.size=size
        self.hash_table=[[] for _ in range(self.size)]
    
    #Making a Hash Function
    def hash_function(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.size
    
    #Return searched value with specific key
    def get_value(self,key):
        hashed_key=self.hash_function(key)
        bucket=self.hash_table[hashed_key]
        
        found_key=False
        for index,element in enumerate(bucket):
            element_key,element_value=element
            if element_key==key:
                found_key=True
                break
        
        if found_key:
            print(element_value)
        else:
            print("Not Found")
    
    #Inserting Value into Hash Table
    def set_values(self,key,value):
        hashed_key=self.hash_function(key)
        bucket=self.hash_table[hashed_key]
        
        found_key=False
        for index,element in enumerate(bucket):
            element_key,element_value=element
            if element_key==key:
                found_key=True
                break
        if found_key:
            bucket[index]=(key,value)
        else:
            bucket.append((key,value))
   
    #Deleting Value of Hash Table
    def del_value(self,key):
        hashed_key=self.hash_function(key)
        bucket=self.hash_table[hashed_key]
        
        found_key=False
        for index,element in enumerate(bucket):
            element_key,element_value=element
            if element_key==key:
                found_key=True
                break
        if found_key:
            bucket.pop(index)
        else:
            print("Key not found")
if __name__=="__main__":
    Hash_Table=HashTable(int(input("Enter size of Hash Table:")))
    Main_menu()