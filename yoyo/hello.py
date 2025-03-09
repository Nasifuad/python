class Node():
    def _init_(self, data):
        self.data= data
        self.next= None
        
class LinkedList():
    def _init_(self):
        self.head= None
    
    def insert(self, data):
        newNode= Node(data)
        newNode.next= self.head
        self.head= newNode
        
    def printList(self):
        temp= self.head
        while(temp):
            print(temp.data)
            temp= temp.next


llist= LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)

llist.printList()