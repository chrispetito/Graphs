class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    island_count = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[x][y]:
                if matrix[x][y] == 1:
                    dft(x, y, matrix, visited)

                    island_count += 1

    return island_count

def dft(x, y, matrix, visited):
    stack = Stack()
    stack.push((x, y))

    while stack.size() > 0:
        vertex = stack.pop()
        x = vertex[0]
        y = vertex[1]

        if not visited[y][x]:
            visited[y][x] = True

            for neighbor in get_neighbors((x, y), matrix):
                stack.push(neighbor)
    return visited

def get_neighbors(vertex, matrix):
    x = vertex[0]
    y = vertex[1]

    neighbors = []

    # North
    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append((x, y-1))

    # South
    if y < len(matrix) - 1 and matrix[y+1][x] == 1:
        neighbors.append((x, y + 1))

    # East
    if x < len(matrix[0]) - 1 and matrix[y][x+1] == 1:
        neighbors.append((x+1, y))

    # West
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append((x-1, y))

    return neighbors
    
islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))