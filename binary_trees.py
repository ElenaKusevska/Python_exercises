class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        if start != None:
            traversal = traversal + str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def depth_first(self, start, traversal):
        traversal = ""
        stack = [start]
        while len(stack) > 0:
            current = stack.pop(-1)
            traversal = traversal + current.value
            print(traversal)
            if current.right != None:
                stack.append(current.right)
            if current.left != None:
                stack.append(current.left)

        return(traversal)


tree = BinaryTree("a")
tree.root.left = Node("b")
tree.root.right = Node("c")
tree.root.left.left = Node("d")
tree.root.left.right = Node("e")
tree.root.right.left = Node("f")
tree.root.right.right = Node("g")

print(tree.preorder_print(tree.root, ""))
print(tree.depth_first(tree.root, ""))
