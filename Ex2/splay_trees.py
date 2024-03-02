class Node:
    """
    A class to represent a node in a binary search tree.
    """

    def __init__(self, key=None):
        """
        Initializes a node with a given key.

        Parameters:
        key (optional): The value to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    """
    A class to represent a Splay Tree.
    """

    def __init__(self):
        """
        Initializes an empty Splay Tree.
        """
        self.root = None

    def insert(self, key):
        """
        Inserts a new node with the given key into the Splay Tree.

        Parameters:
        key: The value to be inserted into the tree.
        """
        n = Node(key)
        temp = self.root
        y = None
        while temp is not None:
            y = temp
            if n.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y
        if y is None:
            self.root = n
        elif n.key < y.key:
            y.left = n
        else:
            y.right = n
        self.root = self.splay(n)

    def rightrotate(self, x):
        """
        Performs a right rotation at the given node.

        Parameters:
        x: The node at which the right rotation is performed.

        Returns:
        The new root of the subtree after rotation.
        """
        y = x.left
        flag = False
        if x.parent is None:
            flag = True
        else:
            temp = x.parent
        sub2 = y.right
        y.right = x
        x.parent = y
        x.left = None
        if sub2 is not None:
            x.left = sub2
            sub2.parent = x
        if flag:
            y.parent = None
        else:
            y.parent = temp
            if temp.left == x:
                temp.left = y
            if temp.right == x:
                temp.right = y
        return y

    def leftrotate(self, x):
        """
        Performs a left rotation at the given node.

        Parameters:
        x: The node at which the left rotation is performed.

        Returns:
        The new root of the subtree after rotation.
        """
        y = x.right
        flag = False
        if x.parent is None:
            flag = True
        else:
            temp = x.parent
        sub2 = y.left
        y.left = x
        x.parent = y
        x.right = None
        if sub2 is not None:
            x.right = sub2
            sub2.parent = x
        if flag:
            y.parent = None
        else:
            y.parent = temp
            if temp.right == x:
                temp.right = y
            if temp.left == x:
                temp.left = y
        return y

    def splay(self, node):
        """
        Performs splaying operation at the given node to bring it to the root.

        Parameters:
        node: The node to be splayed.

        Returns:
        The node after splaying.
        """
        while node.parent is not None:
            if node.parent == self.root:
                if node == node.parent.left:
                    self.rightrotate(node.parent)
                else:
                    self.leftrotate(node.parent)
            else:
                p = node.parent
                g = p.parent
                if node.parent.left == node and p.parent.left == p:
                    self.rightrotate(g)
                    self.rightrotate(p)
                elif node.parent.right == node and p.parent.right == p:
                    self.leftrotate(g)
                    self.leftrotate(p)
                elif node.parent.right == node and p.parent.left == p:
                    self.leftrotate(p)
                    self.rightrotate(g)
                else:
                    self.rightrotate(p)
                    self.leftrotate(g)
        return node

    def preorder(self, root):
        """
        Performs preorder traversal starting from the given root node.

        Parameters:
        root: The root node from which the traversal starts.
        """
        if root is not None:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        """
        Performs inorder traversal starting from the given root node.

        Parameters:
        root: The root node from which the traversal starts.
        """
        if root is not None:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)


if __name__ == "__main__":
    # Test cases
    b = SplayTree()
    values1 = [4, 7, 17, 92, 15, 32, 67, 43, 65, 1]
    for value in values1:
        b.insert(value)
    b.preorder(b.root)
    print()
    b.inorder(b.root)
    
    print()
    print("==================================")
    print()

    b = SplayTree()
    values2 = [400, 217, 17, 922, 15, 32, 67, 43, 65, 1000]
    for value in values2:
        b.insert(value)
    b.preorder(b.root)
    print()
    b.inorder(b.root)
