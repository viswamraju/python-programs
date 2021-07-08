import sys

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, val):
#         if self.root is None:
#             self.root = Node(val)
#             return
#         node = self.root
#         while 1:
#             if val < node.data:
#                 if node.left is not None:
#                     node = node.left
#                 else:
#                     node.left = Node(val)
#                     break
#             elif val > node.data:
#                 if node.right is not None:
#                     node = node.right
#                 else:
#                     node.right = Node(val)
#                     break
#             else:
#                 break

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            node = self.root
            while True:
                if val < node.data:
                    if node.left is None:
                        node.left = Node(val)
                        print("added")
                        break
                    else:
                        node = node.left
                elif val > node.data:
                    if node.right is None:
                        node.right = Node(val)
                        print("added")
                        break
                    else:
                        node = node.right
                else:
                    break

    def in_order_traversal(self, node):
        if node.left:
            self.in_order_traversal(node.left)
        print(node.data)
        if node.right:
            self.in_order_traversal(node.right)

    def search(self, node, val):
        if node.data == val:
            return True

        if val < node.data:
            if node.left:
                return self.search(node.left, val)
            else:
                return False
        elif val > node.data:
            if node.right:
                return self.search(node.right, val)
            else:
                return False

    def find_min(self, ):
        node = self.root

        while True:
            if node.left is None:
                min = node.data
                return min
            else:
                node = node.left

    def find_max(self, ):
        node = self.root

        while True:
            if node.right is None:
                max = node.data
                return max
            else:
                node = node.right

    def delete_node(self, node, val):
        if node is None:
            return

        if node.data == val:
            # 4 possibilites
            # no children
            if not node.left and not node.right:
                return None

            if not node.left and node.right:
                return node.right

            if not node.right and node.left:
                return node.left
            if node.right and node.left:
                pnt = node.right
                while pnt.left:
                    pnt = pnt.left

                node.data = pnt.data
                node.right = self.delete_node(node.right, val)


        elif val < node.data:
            node.left = self.delete_node(node.left, val)
        elif val > node.data:
            node.right = self.delete_node(node.right, val)



tree = Tree()
tree.insert(12)
tree.insert(6)
tree.insert(18)
tree.insert(3)

# tree.in_order_traversal(tree.root)

print(tree.search(tree.root, 20))
print(tree.find_min())
print(tree.find_max())








tree = Tree()
