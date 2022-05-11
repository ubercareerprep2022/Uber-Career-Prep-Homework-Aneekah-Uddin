class LinkedList :
    class Node:
        def __init__(self, value, nextNode = None):
            self.value = value
            self.nextNode = nextNode
        
        def getValue():
            return self.value
        
        def setNext(nextNode) :
            self.nextNode = nextNode
        

        def getNext():
            return self.nextNode
    
    def __init__(self, head = None):
        self.head = head
        self.tail = head
        length = 0

    def push(newNode):
        if head == None:
            head = newNode
        else:
            tail.nextNode = newNode
            tail = tail.nextNode
        length += 1

    def pop():
        curr = head
        for i in range(length - 2):
            curr = curr.nextNode
        temp = curr.nextNode
        curr.nextNode = None
        length -= 1
        return temp

    def insert(index, newNode):
        if (index >= length) :
            return 
        curr = head
        for i in range(index-1):
            curr = curr.nextNode
        temp = curr.nextNode
        curr.nextNode = newNode
        newNode.nextNode = temp
        length += 1

    def remove(index):
        if (index >= length) :
            return 
        curr = head
        for i in range(index-1):
            curr = curr.nextNode
        if (index == length - 1): 
            temp = None
        else:
            temp = curr.nextNode.nextNode
        curr.nextNode = temp
        length -= 1

    def elementAt(index):
        if (index >= length) :
            return None
        curr = head
        for i in range(index-1):
            curr = curr.nextNode
        return curr.nextNode
    
    def size():
        return length
    
    def printList():
        curr = head
        for i in range(length):
            print(curr.getValue)
            curr = curr.nextNode
        
    