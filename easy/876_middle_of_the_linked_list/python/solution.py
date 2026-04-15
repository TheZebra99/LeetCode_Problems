class ListNode:
    def __init__(self, value = 0, next = None): # define constructor
        self.value = value
        self.next = next

class CustomLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, value):
        newNode = ListNode(value)
        if self.head == None:
            self.head = newNode
        else:
            tempNode = self.head
            while tempNode.next is not None:
                tempNode = tempNode.next
            tempNode.next = newNode
        self.size += 1
    
    def printList(self):
        currentNode = self.head
        print ("Linked list: ")
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
    
    def findMiddleNode(self):
        if self.head == None:
            return None
        
        slowPtr = self.head
        fastPtr = self.head

        while fastPtr is not None and fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        return slowPtr
        

if __name__ == '__main__':
    myList = CustomLinkedList()
    myList.insert(5)
    myList.insert(15)
    myList.insert(3)
    myList.printList()
    print("Middle node is " + str(myList.findMiddleNode().value))

    myList.insert(45)
    myList.printList()
    print("Middle node is " + str(myList.findMiddleNode().value))
