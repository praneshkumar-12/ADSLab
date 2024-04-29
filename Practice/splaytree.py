class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
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

    def splay(self, node):
        while node.parent is not None:
            if node.parent == self.root:
                if node == node.parent.left:
                    self.rightrotate(node.parent)
                else:
                    self.leftrotate(node.parent)
            else:
                p = node.parent
                g = p.parent

                if p.left == node and g.left == p:
                    self.rightrotate(g)
                    self.rightrotate(p)
                elif p.right == node and g.right == p:
                    self.leftrotate(g)
                    self.leftrotate(p)
                elif p.left == node and g.right == p:
                    self.rightrotate(p)
                    self.leftrotate(g)
                else:
                    self.leftrotate(p)
                    self.rightrotate(g)

        return node

    def leftrotate(self, x):
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

    def rightrotate(self, x):
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
            x.right = sub2
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

    def preorder(self, root):
        if root is not None:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def __search(self, key, pos=None):
        if pos is None:
            pos = self.root
        if key == pos.key:
            return pos
        elif key < pos.key and pos.left is not None:
            return self.__search(key, pos.left)
        elif key > pos.key and pos.right is not None:
            return self.__search(key, pos.right)
        else:
            print("Element is not in tree!")
            return None

    def find(self, key):
        temp = self.__search(key)

        if temp is not None:
            self.splay(temp)
        else:
            return None

    def delete(self, key):
        search_node = self.__search(key)

        if search_node is None:
            print("Element is not in tree!")
            return None

        self.root = self.splay(search_node)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left

        right_subtree = SplayTree()
        right_subtree.root = self.root.right

        if right_subtree.root is not None:
            right_subtree.root.parent = None

        if left_subtree.root is not None:
            m = left_subtree.find_max(left_subtree.root)
            left_subtree.root = self.splay(m)
            left_subtree.right = right_subtree.root
            self.root = left_subtree.root
        else:
            self.root = right_subtree.root


if __name__ == "__main__":
    # Create a new Splay Tree
    splay_tree = SplayTree()

    # Insert some keys into the tree
    keys_to_insert = [10, 5, 15, 3, 7, 12, 17]
    for key in keys_to_insert:
        splay_tree.insert(key)

    print("Splay Tree after insertion:")
    splay_tree.preorder(splay_tree.root)  # Print the tree in preorder traversal

    # Delete a key from the tree
    key_to_delete = 7
    print(f"\nDeleting key {key_to_delete} from the tree:")
    splay_tree.delete(key_to_delete)

    print(splay_tree.root.key)

    print("\nSplay Tree after deletion:")
    splay_tree.preorder(splay_tree.root)  # Print the tree in preorder traversal
