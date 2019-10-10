import random

def bfs(graph, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    queue = [[starting_vertex]]
    visited = []

    if starting_vertex == destination_vertex:
        return [starting_vertex]

    while queue:
        path = queue.pop(0)                         # pop the first path from queue
        node = path[-1]                     # get the last node from path
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:      # go through all neighbor node
                new_path = list(path)   # construct new
                new_path.append(neighbor)   #add in the neighbors
                queue.append(new_path)

                if neighbor == destination_vertex:  # return path if neighbor equals goal
                    return new_path

            visited.append(node)    # mark as explored

    # Connecting path doesn't exist
    return None

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
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

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
        # Add users
        for i in range(numUsers):
            self.addUser(str(i + 1))

        print("All Users")

        # Create friendships
        all_possible_combinations = []
        for i in range(numUsers):
            for j in range(numUsers):
                if i < j:
                    all_possible_combinations.append((i + 1, j + 1))

        print("List of all possible combinations")
        print(all_possible_combinations)
        random.shuffle(all_possible_combinations)
        num_friendships = numUsers * avgFriendships
        for userID, friendID in all_possible_combinations[:num_friendships]:
            self.addFriendship(userID, friendID)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        for friendID in self.users.keys():
            path = bfs(self.friendships, userID, friendID)
            if path is not None: # path exists
                visited[friendID] = path        

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    print("Start of Populate Graph")
    sg.populateGraph(10, 2)
    print(sg.friendships)
    print("Start of Get All Social")
    connections = sg.getAllSocialPaths(2)
    print(connections)
