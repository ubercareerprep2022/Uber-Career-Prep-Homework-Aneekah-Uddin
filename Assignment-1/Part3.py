class Stack:
    stackArr = []
    length = 0

    def __init__(self):
        pass 

    def push(newItem) :
        stackArr.append(newItem)
        length += 1
    
    def pop() :
        ret = stackArr[-1]
        stackArr = stackArr[:-1]
        length -= 1
        return ret
    
    def top() :
        return stackArr[-1]
    
    def isEmpty() :
        if length == 0 :
            return true
        return false
    
    def size() :
        return length

class Queue:
    queueArr = []
    length = 0

    def __init__(self):
        pass 

    def enqueue(itemAdd):
        queueArr.append(itemAdd)
        length += 1

    def dequeue():
        ret = queueArr[0]
        queueArr = queueArr[1:]
        length -= 1
        return ret
    
    def rear():
        if length == 0:
            return -1
        return queue[-1]

    def front():
        if length == 0:
            return -1
        return queue[0]

    def size():
        return length

    def isEmpty():
        if length == 0 :
            return true
        return false