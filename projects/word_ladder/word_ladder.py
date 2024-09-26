f = open('words.txt', 'r')
words = f.read().split('\n')

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = ''.join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors

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

def find_word_ladder(beginWord, endWord):
    #     #   Create a queue
    #     queue = Queue()
    # #   Create list of visited nodes
    #     visited = set()
    # #   Put starting node in the queue
    #     queue.enqueue([starting_vertex])
    # #   While: queue not empty
    #     while queue.size() > 0:
    # #   Pop first node out of queue
    #         path = queue.dequeue()
    #         vertex = path[-1]
    # #   If not visited
    #         if vertex not in visited:
    #             if vertex == destination_vertex:
    #                 return path
    #             visited.add(vertex)
    #             # print(vertex)
    # #   Mark as visited
    # #   Get adjacent edges and add to list
    #             for next_vert in self.vertices[vertex]:
    #                 new_path = list(path)
    #                 new_path.append(next_vert)
    #                 queue.enqueue(new_path)
    #                 # if next_vert == destination_vertex:
    #                 #     return next_vert
    # #   Goto top of loop    
    queue = Queue()
    visited = set()
    queue.enqueue([beginWord])
    while queue.size() > 0:
        path = queue.dequeue()
        word = path[-1]
        if word not in visited:
            if word == endWord:
                return path
            visited.add(word)
            for next_word in get_neighbors(word):
                new_path = list(path)
                new_path.append(next_word)
                queue.enqueue(new_path)

print(find_word_ladder('sail', 'boat'))