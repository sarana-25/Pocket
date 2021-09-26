class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    
    def addChildNode(self,data):
        if self.data:
            if data==self.data:
                return
            elif data<self.data:
                if self.left is None:
                    self.left=BinaryTree(data)
                else:
                    self.left.addChildNode(data)
            else:
                if self.right is None:
                    self.right=BinaryTree(data)
                else:
                    self.right.addChildNode(data)
        else:
            self.data=data
    
    def search(self,value):
        if self.data==value:
            print("Found")
            return
        if value<self.data:
            if self.left is not None:
                self.left.search(value)
            else:
                print("Not Found")
        else:
            if self.right is not None:
                self.right.search(value)
            else:
                print("Not Found")

    def delete(self,value,root):
        if root==None:
            return root
        if value==root.data:
            if root.left==None:
                root=root.right
            elif root.right==None:
                root=root.left
            else:
                root=self.findnext(root)
                root.right=self.delete(root.right,root.data)

   
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
    def inOrderTraversal(self,root):
        element=[]
        if root:
            element+=self.inOrderTraversal(root.left)
            element.append(root.data)
            element+=self.inOrderTraversal(root.right)
        return element
    
    def preOrderTraversal(self,root):
        element=[]
        if root:
            element.append(root.data)
            element+=self.preOrderTraversal(root.left)
            element+=self.preOrderTraversal(root.right)
        return element

    def postOrderTraversal(self,root):
        element=[]
        if root:
            element=self.postOrderTraversal(root.left)
            element+=self.postOrderTraversal(root.right)
            element.append(root.data)
        return element
    
if __name__=="__main__":
    n=int(input("No of nodes:"))
    lst=[]
    for _ in range(n):
        lst.append(input())
    root=BinaryTree(lst[0])
    for i in range(1,n):
        root.addChildNode(lst[i])
    print("In Order Traversal:",root.inOrderTraversal(root))
    # print("Pre Order Traversal:",root.preOrderTraversal(root))
    # print("Post Order Traversal:",root.postOrderTraversal(root))
    # root.search(input("Enter what you want to search:"))
    # print(root.find_max())
    # print(root.find_min())
    root.delete(input("Enter the data you want to delete:"),root)
    print("In Order Traversal:",root.inOrderTraversal(root))
