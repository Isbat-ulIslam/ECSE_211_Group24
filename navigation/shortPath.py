import heapq

class Node:
    """
    Represents a node in the A* search algorithm.

    Attributes:
        x (int): X-coordinate of the node.
        y (int): Y-coordinate of the node.
        parent (Node): Parent node in the search tree.
        g (float): Cost from the start node to this node.
        h (float): Heuristic (Manhattan distance) from this node to the goal.
        f (float): Total cost (g + h) for this node.
    """

    def __init__(self, x, y):
        """
        Initializes a new Node with the given coordinates.

        Args:
            x (int): X-coordinate of the node.
            y (int): Y-coordinate of the node.
        """
        self.x = x
        self.y = y
        self.parent = None
        self.g = float('inf')
        self.h = float('inf')
        self.f = float('inf')

    def __lt__(self, other):
        """
        Compares two nodes based on their f values.

        Args:
            other (Node): Another node to compare.

        Returns:
            bool: True if this node's f value is less than the other node's f value, otherwise False.
        """
        return self.f < other.f

def manhattan_distance(node1, node2):
    """
    Calculates the Manhattan distance between two nodes.

    Args:
        node1 (Node): The first node.
        node2 (Node): The second node.

    Returns:
        int: The Manhattan distance between the two nodes.
    """
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def astar(start, end, obstacles):
    """
    Finds the shortest path from the start node to the end node using the A* search algorithm.

    Args:
        start (tuple): The starting coordinates (x, y).
        end (tuple): The destination coordinates (x, y).
        obstacles (set): A set of obstacle coordinates (x, y).

    Returns:
        list or None: A list of coordinates representing the shortest path from start to end, or None if no path is found.
    """
    open_set = []  
    closed_set = set()
    start_node = Node(*start)
    end_node = Node(*end)
    start_node.g = 0
    start_node.h = manhattan_distance(start_node, end_node)
    start_node.f = start_node.h
    heapq.heappush(open_set, start_node)

    while open_set:
        current = heapq.heappop(open_set)

        if current.x == end[0] and current.y == end[1]:
            path = []
            while current:
                path.insert(0, (current.x, current.y))
                current = current.parent
            return path
        
        closed_set.add((current.x, current.y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor_x, neighbor_y = current.x + dx, current.y + dy
            if (0 <= neighbor_x <= 3) and (0 <= neighbor_y <= 3) and (neighbor_x, neighbor_y) not in obstacles:
                neighbor = Node(neighbor_x, neighbor_y)
                if (neighbor_x, neighbor_y) in closed_set:
                    continue

                tentative_g = current.g + 1
                if tentative_g < neighbor.g:
                    neighbor.parent = current
                    neighbor.g = tentative_g
                    neighbor.h = manhattan_distance(neighbor, end_node)
                    neighbor.f = neighbor.g + neighbor.h
                    heapq.heappush(open_set, neighbor)

    return None
