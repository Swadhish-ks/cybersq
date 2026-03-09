class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 'right'

    def is_valid(self):
        # Check valid state (no side has more cannibals than missionaries)
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if (self.missionaries > 0 and self.missionaries < self.cannibals):
            return False
        m_right = 3 - self.missionaries
        c_right = 3 - self.cannibals
        if (m_right > 0 and m_right < c_right):
            return False
        return True

    def generate_children(self):
        children = []
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible moves
        for m, c in moves:
            if self.boat == 'left':
                new_state = State(self.missionaries - m, self.cannibals - c, 'right', self)
            else:
                new_state = State(self.missionaries + m, self.cannibals + c, 'left', self)
            if new_state.is_valid():
                children.append(new_state)
        return children

    def __repr__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.boat})"


def bfs():
    initial = State(3, 3, 'left')
    queue = [initial]
    visited = []

    while queue:
        current = queue.pop(0)
        if current.is_goal():
            path = []
            while current:
                path.append(current)
                current = current.parent
            return path[::-1]  # reverse path

        for child in current.generate_children():
            if child.__repr__() not in visited:
                visited.append(child.__repr__())
                queue.append(child)
    return None


path = bfs()
for state in path:
    print(state)