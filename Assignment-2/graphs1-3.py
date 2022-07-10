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

# Exercise 4 - Minimum number of edges between two nodes of a Graph
    # perform BFS and keep track of edge count, until you find the right node

    def minNumberOfEdges(self, start, target):
        # add the first nodes edges to queue
        nextLevelNodes = self.adj_list[start]
        count = 1
        # increase count by one
        # iterate through the queue
        while (nextLevelNodes):
            # iterate thru that level
            currLevelLength = len(nextLevelNodes)
            for i in range(currLevelLength):
                # if found, return count
                if nextLevelNodes[0].val == target.val:
                    return count
                # else, add the nodes in the adj list
                else:
                    nextLevelNodes.append(self.adj_list[nextLevelNodes[0]])
                nextLevelNodes.pop(0)
            # update the count
            count += 1    
        # return -1 if not found
        return -1

# Exercise 5 - Loop in a Directed Graph
    def validCourses(numCourses, prereqs):
        # put information into a graph structure w / adj list
        adj_list = [0] * len(numCourses) * len(numCourses)
        inDegree = [0] * len(numCourses)
        visited = [0] * len(numCourses)

        for prereq in prereqs:
            adj_list[ (prereq[0] * len(numCourses)) + prereq[1]] = 1
            inDegree[prereq[1]] += 1

        # topological sort not possible in rooted DAG - if indeg of any number is greater than 0 after finishing
        queue = []
        for i in range(numCourses):
            if (inDegree[i] == 0):
                queue.append(i)
                visited[i] = True
        
        while queue:
            curr = queue.pop(0)
            for i in range(numCourses):
                if adj_list(curr * len(numCourses) + i) and visited(i) == False:
                    inDegree[i] -= 1
                    if inDegree[i] == 0:
                        visited[i] = True
                        queue.append(i)
        
        for i in range(numCourses):
            if inDegree[i] != 0:
                return False
        
        return True

