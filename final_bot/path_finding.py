import heap

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def compare(parent, child):
    return parent.f <= child.f

def astar(maze, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_heap = heap.Heap(compare)
    closed_list = [[0 for i in range(len(maze))] for i in range(len(maze))]
    open_list = [[0 for i in range(len(maze))] for i in range(len(maze))]

    # Add the start node
    open_heap.add(start_node)
    x,y = start_node.position
    open_list[x][y] = 1

    # Loop until you find the end
    while not open_heap.is_empty():

        # Get the current node

        # Pop current off open list, add to closed list
        current_node = open_heap.del_min()
        x,y = current_node.position
        closed_list[x][y] = 1
        open_list[x][y] = 0

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != True:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            x,y = child.position
            if closed_list[x][y]:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if open_list[x][y]:
                continue

            # Add the child to the open list
            open_heap.add(child)
            x,y = child.position

            open_list[x][y] = 1
