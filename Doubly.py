class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def addInFirst(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return self.head
        else:
            newNode.next=self.head
            self.head.pre=newNode
            self.head=newNode

    def addInLast(self,data):
        temp=self.head
        newNode=Node(data)
        if(self.head is None):
            head=newNode
            return
        else:
            while(temp.next is not None):
                temp=temp.next
        
        temp.next=newNode
        newNode.pre=temp

    def addInMiddle(self,data,idx):
        newNode=Node(data)
        temp=self.head
        count=1
        if(idx==1):
            self.addInFirst(data)
        else:
            while(count<idx-1 and temp.next is not None):
                temp=temp.next
                count+=1
            
            if temp.next is None or temp is None:
                print("Out of scope Insrtion is not possible")
                return
            else:
                newNode.next=temp.next
                temp.next.pre=newNode
                temp.next=newNode
    
    def delInLast(self):
        if self.head is None:
            return "Deletion not possible linked list is empty"
        else:
            temp=self.head
            while(temp.next.next is not None):
                temp=temp.next
        
            temp.next.pre=None
            temp.next=None
            
    def delInFirst(self):
        if self.head is None:
            return "Deltion is not possible linked list is empty"
        else:
            self.head=self.head.next
            self.head.pre=None

    def delInMiddle(self,idx):
        temp=self.head
        count=1
        if(idx==1):
            self.delInFirst()
        else:
            while(count<idx-1 and temp.next is not None):
                temp=temp.next
                count+=1
            
            if temp.next is None or temp is None:
                print("Out of scope deletion is not possible")
                return
            else:
                temp.next=temp.next.next
                temp.next.pre=temp
    
        
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next
        print()

doubly=DoublyLinkedList();
doubly.addInFirst(20)
doubly.addInFirst(22)
doubly.addInFirst(25)
doubly.print()
doubly.addInLast(23)
doubly.print()
# doubly.addInMiddle(10,6)
# doubly.print()
# doubly.delInFirst()
# doubly.print()
# doubly.delInLast()
# doubly.print()
doubly.delInMiddle(2)
doubly.print()
    