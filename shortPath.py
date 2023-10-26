import heapq;

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.g = float('inf')
        self.h = float('inf')
        self.f = float('inf')

    def __lt__(self, other):
        return self.f < other.f
    

def manhattan_distance(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def astar(start, end, obstacles):
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

fire_station = (0, 0)
destination = (3, 3)
obstacles = {(2, 2)}

path = astar(fire_station, destination, obstacles)

if path:
    print("Shortest path: ", path)
else:
    print("No path found")