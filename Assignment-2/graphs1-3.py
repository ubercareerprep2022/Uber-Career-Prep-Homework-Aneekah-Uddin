# Graphs - Exercises 1-3
# Exercise 1: Implement a graph using adjacency list

class GraphNode:
    def __init__(self, val):
        self.val = val

class GraphWithAdjacencyList:
    def __init__(self):
        self.adj_list = {}
        self.keyToNode = {}

    def addNode(self, key):
        node = GraphNode(key)
        self.adj_list[node] = []
        self.keyToNode[key] = node

    def removeNode(self, key):
        removalNode = self.keyToNode[key]
        connectedNodes = self.adj_list[removalNode]
        for node in connectedNodes:
            self.adj_list[node] = self.adj_list[node].remove(removalNode)
        del self.adj_list[removalNode]
        del removalNode
    
    def addEdge(self, node1, node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
    
    def removeEdge(self, node1, node2):
        node1 = self.keyToNode[node1]
        node2 = self.keyToNode[node2]
        self.adj_list[node1].remove(node2)
        self.adj_list[node2].remove(node1)
    
    def getAdjNodes(self, key):
        return self.adj_list[self.keyToNode[key]]
    
    # Exercise 2: DFS Traversal
    def dfs(self, key):
        check = set()
        dfsRecursive(self.keyToNode(key))
        
        def dfsRecursive(node, check):
            if check.contains(node) == False:
                print(node.val)
                check.add(node)
                for n in self.adj_list[node]:
                    dfsRecursive(n, check)
    
    #Exercise 3: BFS Traversal
    def bfs(self, key):
        queue = [self.keyToNode(key)]
        check = set()
        while queue:
            node = queue.pop(0)
            if check.contains(node) == False:
                print(node.val)
                check.add(node)
                for n in self.adj_list[node]:
                    queue.append(n)


    