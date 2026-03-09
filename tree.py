class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.value!r})"
    
    
## create tree structure    
root = TreeNode("Root")

# Level 1 children
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")

# Level 2 children
child4 = TreeNode("Child 4")
child5 = TreeNode("Child 5")
child6 = TreeNode("Child 6")

# Level 3 children
child7 = TreeNode("Child 7")
child8 = TreeNode("Child 8")

# level 4 children

child9 = TreeNode("Child 9")
child10 = TreeNode("Child 10")



# Build the tree
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
root.add_child(child4)
root.add_child(child5)
root.add_child(child6)
root.add_child(child7)
root.add_child(child8)
root.add_child(child9)
root.add_child(child10) 
print(root.children)
