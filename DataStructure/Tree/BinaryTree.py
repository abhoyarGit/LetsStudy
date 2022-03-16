class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #Visit Left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #Base
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data :
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_binary_tree(lst):
    root = BinaryTreeNode(lst[0])
    for i in range(1,len(lst)):
        root.add_child(lst[i])

    return root


if __name__ == "__main__":
    numbers = [1,2,33,99,10,4,55,66,77,77]
    numbers_Tree = build_binary_tree(numbers)
    print(numbers_Tree.in_order_traversal())
    print(numbers_Tree.search(99))