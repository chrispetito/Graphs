class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Cannot create edge based on given vertices!')
        

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    
    for node in ancestors:
        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
        graph.add_edge(node[1], node[0])

    queue = Queue()
    queue.enqueue([starting_node])

    maxpath = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        path = queue.dequeue()
        node = path[-1]
        if len(path) > maxpath:
            maxpath = len(path)
            earliest_ancestor = node
        elif len(path) == maxpath:
            if node < maxpath:
                maxpath = len(path)


        for next_word in graph.vertices[node]:
            new_path = list(path)
            new_path.append(next_word)
            queue.enqueue(new_path)
    return node
