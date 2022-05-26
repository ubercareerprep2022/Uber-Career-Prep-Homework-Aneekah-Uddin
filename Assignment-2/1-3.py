class Tree:
    def __init__ (self, root):
        self.root = root
    
    # Exercise 1
    def printTree(self):
        queue = [self.root]
        while (len(queue) != 0) :
            print(queue[0].data)
            if (queue[0].left != None):
                queue.append(queue[0].left)
            if (queue[0].right != None):
                queue.append(queue[0].right)
            queue = queue[1:]


class TreeNode:
    def __init__(self, data, left=None, right=None) :
        self.data = data
        self.left = left
        self.right = right
    
leftChild = TreeNode(6)
rightChild = TreeNode(3)
left = TreeNode(7)
right = TreeNode(17, leftChild, rightChild)
root = TreeNode(1, left, right)
tree = Tree(root)

tree.printTree()

class OrganizationStructure:
    def __init__ (self, ceo):
        self.ceo = ceo
    
    def printLevelByLevel(self):
        queue = [self.ceo]
        while (len(queue) != 0) :
            print("Name: " + queue[0].name + ", Title: " + queue[0].title)
            if (queue[0].directReports != None):
                for x in queue[0].directReports :
                    queue.append(x)
            queue = queue[1:]
    
    def recur(self, employee, level) :
        if (employee == None) :
            return level
        if (employee.directReports == None):
            return level
        maxlevel = level
        for x in employee.directReports:
            newlevel = self.recur(x, level + 1)
            if newlevel > maxlevel :
                maxlevel = newlevel
        return maxlevel

    def printNumLevels(self):
        level = 0
        print(self.recur(self.ceo, level + 1))

class Employee:
    def __init__(self, name, title, directReports) :
        self.name = name
        self.title = title
        self.directReports = directReports

k = Employee("k", "sales intern", None)
j = Employee("j", "sales rep", [k])
i = Employee("i", "director", [j])
f = Employee("f", "engineer", None)
g = Employee("g", "engineer", None)
h = Employee("h", "engineer", None)
d = Employee("d", "manager", [f, g, h])
e = Employee("e", "manager", None)
b = Employee("b", "cfo", [i])
c = Employee("c", "cto", [d,e])
a = Employee("a", "ceo", [b,c])
org = OrganizationStructure(a)

org.printLevelByLevel()
org.printNumLevels()


