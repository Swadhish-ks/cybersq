from collections import deque

CAP_A = 4  # 4L jug
CAP_B = 3  # 3L jug
TARGET = 2  # target liters in jug A


class State:
    def __init__(self, a, b, parent=None, action=None):
        self.a = a
        self.b = b
        self.parent = parent
        self.action = action

    def is_goal(self):
        return self.a == TARGET

    def is_valid(self):
        return 0 <= self.a <= CAP_A and 0 <= self.b <= CAP_B

    def generate_children(self):
        children = []
        a, b = self.a, self.b

        # Fill A
        if a < CAP_A:
            children.append(State(CAP_A, b, self, "Fill A"))

        # Fill B
        if b < CAP_B:
            children.append(State(a, CAP_B, self, "Fill B"))

        # Empty A
        if a > 0:
            children.append(State(0, b, self, "Empty A"))

        # Empty B
        if b > 0:
            children.append(State(a, 0, self, "Empty B"))

        # Pour A -> B
        transfer = min(a, CAP_B - b)
        if transfer > 0:
            children.append(State(a - transfer, b + transfer, self, f"Pour A->B ({transfer}L)"))

        # Pour B -> A
        transfer = min(b, CAP_A - a)
        if transfer > 0:
            children.append(State(a + transfer, b - transfer, self, f"Pour B->A ({transfer}L)"))

        # keep only valid children
        return [c for c in children if c.is_valid()]

    def __repr__(self):
        return f"({self.a}L, {self.b}L)"


def bfs(start=(0, 0)):
    initial = State(*start)
    queue = deque([initial])
    visited = {repr(initial)}

    while queue:
        current = queue.popleft()
        if current.is_goal():
            # reconstruct path
            path = []
            node = current
            while node:
                path.append(node)
                node = node.parent
            return list(reversed(path))
        for child in current.generate_children():
            r = repr(child)
            if r not in visited:
                visited.add(r)
                queue.append(child)
    return None


if __name__ == "__main__":
    path = bfs((0, 0))
    if not path:
        print("No solution found.")
    else:
        print("Steps to get 2L in 4L jug:")
        for st in path:
            act = st.action or "Start"
            print(f"{act:18} -> {st}")