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

        if vertex not in self.vertices:
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
    # create graph
    graph = Graph()

    # add vertices and edges to graph
    for node in ancestors:
        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
        graph.add_edge(node[1], node[0])

    # create queue and enqueue starting_node
    queue = Queue()
    queue.enqueue([starting_node])

    # define max path length and earliest ancestor
    maxpath = 1
    earliest_ancestor = -1

    # if queue size is greater than 0, set path to dequeue and vertext to path[-1]
    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]

        # if the path length is greater than or equal to maxpath and vertex is smaller than earlier ancestor
        # or path length is greater than maxpath...
        if (len(path) >= maxpath and vertex < earliest_ancestor) or len(path) > maxpath:
            # set earliest ancestor to maxpath and maxpath to path length
            earliest_ancestor = vertex
            maxpath = len(path)

        # for each neighbor in graph vertices...
        for neighbor in graph.vertices[vertex]:
            # create new path, add neighbor to new path, and enqueue new path
            new_path = list(path)
            new_path.append(neighbor)
            queue.enqueue(new_path)

    return earliest_ancestor
