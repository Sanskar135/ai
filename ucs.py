from queue import PriorityQueue

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def get_children(self):
        children = []
        x, y = self.find_blank()
        if x > 0:
            children.append(self.create_child(x, y, x-1, y, "Up"))
        if y > 0:
            children.append(self.create_child(x, y, x, y-1, "Left"))
        if x < 2:
            children.append(self.create_child(x, y, x+1, y, "Down"))
        if y < 2:
            children.append(self.create_child(x, y, x, y+1, "Right"))
        return children

    def create_child(self, x1, y1, x2, y2, action):
        child_state = [row[:] for row in self.state]
        child_state[x1][y1], child_state[x2][y2] = child_state[x2][y2], child_state[x1][y1]
        child = Node(child_state, self, action, self.path_cost+1)
        return child

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

def uniform_cost_search(initial_state):
    frontier = PriorityQueue()
    explored = set()
    frontier.put(Node(initial_state, None, None, 0))
    while not frontier.empty():
        node = frontier.get()
        if node.state == goal_state:
            return node
        explored.add(node)
        for child in node.get_children():
            if child not in explored:
                frontier.put(child)
    return None

solution_node = uniform_cost_search(initial_state)
if solution_node is not None:
    actions = []
    node = solution_node
    while node.action is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    print("Solution path: ", actions)
else:
    print("No solution found.")
