class AdjacencyMatrix:
    def __init__(self):
        self.vertices = []
        self.matrix = [] 
    def addVertex(self,v):
        # initialize if empty
        if self.vertices == []:
            self.vertices = [v]
            self.matrix = [[0]]
        else:
            if v in self.vertices:
                print(f"Vertex {v} already exists.")
                return
            self.vertices.append(v)
            size = len(self.matrix)
            for i in range(size):
                self.matrix[i].append(0)
            self.matrix.append([0 for x in range(size + 1)])
    def addEdge(self,v1,v2,w=1):
        # check the valididty of vertex
        if v1 not in  self.vertices or v2 not in self.vertices:
            if v1 not in self.vertices:
                print(f"Vertex {v1} does not exist.")
            if v2 not in self.vertices:
                print(f"Vertex {v2} does not exist.")
            return
        dictionary = {}
        for i in range(len(self.vertices)):
            dictionary[self.vertices[i]] = i
        # bidirectional
        self.matrix[dictionary[v1]][dictionary[v2]] = w
        self.matrix[dictionary[v2]][dictionary[v1]] = w    
    def printGraph(self):
        # vertices
        print("  ",end="")
        for a in self.vertices:
            print(a,end=" ")
        print()
        # vertex, matrix
        for a in range(len(self.matrix)):
            print(self.vertices[a],end=" ")
            for b in range(len(self.matrix)):
                print(self.matrix[b][a],end=" ")
            print()
            
# dictionary for running functions
run = {
    "1":lambda x: adjMat1.addVertex(input("Enter Vertex: ")),
    "2":lambda x: adjMat1.addEdge(input("Enter Vertex 1: "),input("Enter Vertex 2: "),int(input("Enter Weight: "))),
    "3":lambda x: adjMat1.printGraph()
}

adjMat1 = AdjacencyMatrix()

while True:
    print("--------------")
    print("1. addVertex()")
    print("2. addEdges()")
    print("3. printGraph()")
    run[input("> ")](0)