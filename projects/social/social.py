import random

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


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # add users for range of numUsers
        for i in range(numUsers):
            self.addUser(i)
        # create friendships list

        # target_friendships = numUsers * avgFriendships
        # total_friendships = 0
        # collisions = 0

        # while total_friendships < target_friendships:
        #     userID = random.randint(1, self.lastID)
        #     friendID = random.randint(1, self.lastID)
        #     if self.addFriendship(userID, friendID):
        #         total_friendships += 2
        #     else:
        #         collisions += 1

        # print(f'collisions: {collisions}')

        friendships = []
        # for every user in users dict...
        for user in self.users:
            # and for every friend in range from user to lastID...
            for friend in range(user + 1, self.lastID + 1):
                # add user to friendships list
                friendships.append(( user, friend ))
            # shuffle friendships
        random.shuffle(friendships)
        # for every index in range from 0 to numUsers...
        for j in range(numUsers * avgFriendships // 2):
            # set var to to current friend and add friendship
            curr_friend = friendships[j]
            self.addFriendship(curr_friend[0], curr_friend[1])
                    
        # Add users

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        queue = Queue()
    #   Create list of visited nodes
    #   Put starting node in the queue
        queue.enqueue([userID])
    #   While: queue not empty
        while queue.size() > 0:
    #   Pop first node out of queue
            path = queue.dequeue()
            vertex = path[-1]
    #   If not visited
            if vertex not in visited:
                visited[vertex] = path
                # print(vertex)
    #   Mark as visited
    #   Get adjacent edges and add to list
                for next_vert in self.friendships[vertex]:
                    new_path = path.copy()
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
