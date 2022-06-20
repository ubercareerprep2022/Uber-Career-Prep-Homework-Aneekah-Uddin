# Assignment 2 Exercises 4-6
# Exercise 4 - Build a Binary Search Tree - Code Insert() and Find()

import time
class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    # As Mentioned in the API/Specs
    def insert(self, key):
        self.insertKey(key, self.root)
    
    def find(self, key):
        self.findKey(key, self.root)
    
    # Helper Functions
    def insertKey(self, key, node):
        if key > node.value:
            if node.right == None:
                node.right = Node(key)
            else:
                self.insertKey(key, node.right)
        else:
            if node.left == None:
                node.left = Node(key)
            else:
                self.insertKey(key, node.left)
    
    def findKey(self, key, node):
        if node == None:
            return False
        elif key == node.value:
            return True
        elif key > node.value:
            self.findKey(key, node.right)
        else:
            self.findKey(key, node.left)
    
class Node:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value
    
    
# Exercise 5 - Implement a Phone Book
class Entry:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class ListPhoneBook:
    def __init__(self):
        self.size = 0
        self.book = []

    def size(self):
        return self.size

    def insert(self, name, phoneNumber):
        self.book.append(Entry(name, phoneNumber))
        self.size += 1
    
    def find(self, name):
        for value in self.book:
            if value.name == name:
                return value.number
        return -1

class pBBinarySearchTree:
    def __init__(self, root):
        self.root = pBNode(root)

    # As Mentioned in the API/Specs
    def insert(self, key, number):
        self.insertKey(key, number, self.root)
    
    def find(self, key):
        self.findKey(key, self.root)
    
    # Helper Functions
    def insertKey(self, key, number, node):
        if key > node.value:
            if node.right == None:
                node.right = pBNode(key, number)
            else:
                self.insertKey(key, node.right)
        else:
            if node.left == None:
                node.left = pBNode(key, number)
            else:
                self.insertKey(key, node.left)
    
    def findKey(self, key, node):
        if node == None:
            return False
        elif key == node.value:
            return node.number
        elif key > node.value:
            self.findKey(key, node.right)
        else:
            self.findKey(key, node.left)
    
class pBNode:
    def __init__(self, value, number = None, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value   
        self.number = number

class BinarySearchTreePhoneBook:
    def __init__(self):
        self.size = 0
        self.tree = None

    def size(self):
        return self.size
    
    def insert(self, name, phoneNumber):
        if self.tree == None:
            self.tree = pBBinarySearchTree(pBNode(name, phoneNumber))
        else:
            self.tree.insert(name, phoneNumber)
        
    def find(self, name):
        if self.tree == None:
            return -1
        else:
            return self.tree.find(name)

# Exercise 6
def testPhoneBook(phoneBook):
    tic = time.perf_counter()
    with open('data.csv') as f:
        while True:
            line = f.readline()
            if not line: 
                break
            entry = line.split(',')
            phoneBook.insert(entry[0], entry[1])
    print("Insert took " + str(time.perf_counter() - tic) + " seconds")
    print(phoneBook.size)

    tic = time.perf_counter()
    totalFound = 0
    with open('search.txt') as g:
        while True:
            line = g.readline()
            if not line: 
                break

            if phoneBook.find(line.strip()) == -1:
                print(totalFound)
                raise ValueError("Not found")
            else:
                totalFound += 1
    print("Search took " + str(time.perf_counter() - tic) + " seconds")
    print(totalFound)

print("Testing ListPhoneBook: ")
lpb = ListPhoneBook()
testPhoneBook(lpb)

# issue with the comparator -- in python you cannot use <,>,= to cmp strings
print("Testing BinarySearchTreePhoneBook: ")
bstpb = BinarySearchTreePhoneBook()
testPhoneBook(bstpb)
