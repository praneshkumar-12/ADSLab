# -*- coding: utf-8 -*-
class BPlusTreeNode:
    """
    Represents a node in the B+ Tree.

    Attributes:
    - keys: List of keys stored in the node.
    - children: List of child nodes.
    - is_leaf: Boolean indicating if the node is a leaf node.
    - next_leaf: Reference to the next leaf node (for leaf nodes).
    - parent: Reference to the parent node.
    """

    def __init__(self, is_leaf=True):
        """
        Constructor for the BPlusTreeNode class.

        Parameters:
        - is_leaf: Boolean indicating if the node is a leaf node.
        """
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf
        self.next_leaf = None  # For leaf nodes
        self.parent = None


class BPlusTree:
    """
    Represents a B+ Tree data structure.
    """

    def __init__(self, order):
        """
        Constructor for the BPlusTree class.

        Parameters:
        - order: The order of the B+ Tree.
        """

        self.root = BPlusTreeNode()
        self.order = order

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node.is_leaf:
            for k in node.keys:
                if k == key:
                    return True
            return False
        else:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            return self._search(node.children[i], key)

    def searchkey(self, key):
        """
        Searches for a key in the B+ Tree and returns a message.

        Parameters:
        - key: The key to search for.

        Returns:
        - Message indicating if the key is found or not.
        """
        l1 = self.inorder_traversal()
        if key in l1:
            return f"{key} found in the B+ tree."
        else:
            return f"{search_key}  not found in the B+ tree."

    def insert(self, key):
        """
        Inserts a key into the B+ Tree.

        Parameters:
        - key: The key to be inserted.
        """
        if key is None:
            raise ValueError("Key cannot be None")
        self._insert(self.root, key)

    def _insert(self, node, key):
        """
        Recursively inserts a key into the B+ Tree.

        Parameters:
        - node: The current node being processed.
        - key: The key to be inserted.
        """
        if node.is_leaf:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            node.keys.insert(i, key)

            if len(node.keys) > self.order:
                self._split_leaf(node)
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            self._insert(node.children[i], key)

    def _split_leaf(self, node):
        """
        Splits a leaf node in the B+ Tree.

        Parameters:
        - node: The node to be split.
        """
        mid = len(node.keys) // 2
        new_leaf = BPlusTreeNode(is_leaf=True)
        new_leaf.keys = node.keys[mid:]
        node.keys = node.keys[:mid]

        new_leaf.next_leaf = node.next_leaf
        node.next_leaf = new_leaf

        if node.parent is None:
            new_root = BPlusTreeNode(is_leaf=False)
            new_root.keys = [new_leaf.keys[0]]
            new_root.children = [node, new_leaf]
            node.parent = new_root
            new_leaf.parent = new_root
            self.root = new_root
        else:
            index = self._get_index(node.parent, new_leaf.keys[0])
            node.parent.keys.insert(index, new_leaf.keys[0])
            node.parent.children.insert(index + 1, new_leaf)
            new_leaf.parent = node.parent

            if len(node.parent.keys) > self.order:
                self._split_non_leaf(node.parent)

    def _split_non_leaf(self, node):
        """
        Splits a non-leaf node in the B+ Tree.

        Parameters:
        - node: The node to be split.
        """
        mid = len(node.keys) // 2
        new_node = BPlusTreeNode(is_leaf=False)
        new_node.keys = node.keys[mid + 1 :]
        node.keys = node.keys[:mid]

        new_node.children = node.children[mid + 1 :]
        node.children = node.children[: mid + 1]

        for child in new_node.children:
            child.parent = new_node

        if node.parent is None:
            new_root = BPlusTreeNode(is_leaf=False)
            new_root.keys = [node.keys[-1]]
            new_root.children = [node, new_node]
            node.parent = new_root
            new_node.parent = new_root
            self.root = new_root
        else:
            index = self._get_index(node.parent, node.keys[0])
            node.parent.keys.insert(index, node.keys[-1])
            node.parent.children.insert(index + 1, new_node)
            new_node.parent = node.parent

            if len(node.parent.keys) > self.order:
                self._split_non_leaf(node.parent)

    def _get_index(self, node, key):
        """To get the index of any key value"""
        index = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1
        return index

    def inorder_traversal(self):
        """To perform the inorder traversal"""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            if node.is_leaf:
                for key in node.keys:
                    result.append(key)
            else:
                for i, child in enumerate(node.children):
                    if i > 0:
                        result.append(node.keys[i - 1])
                    self._inorder_traversal(child, result)

    def print_leaf_keys(self):
        """To print the keys in the leaf nodes"""
        leaf_keys = []
        self._get_leaf_keys(self.root, leaf_keys)
        print("Keys in Leaf Nodes:", leaf_keys)

    def _get_leaf_keys(self, node, leaf_keys):
        if node is not None:
            if node.is_leaf:
                for key in node.keys:
                    leaf_keys.append(key)
            else:
                for child in node.children:
                    self._get_leaf_keys(child, leaf_keys)


# Driver code
if __name__ == "__main__":
    bplus_tree = BPlusTree(order=3)

    keys_to_insert = [10, 15, 1, 16, 7, 25, 23, 17, 18, 9, 28, 24]
    for key in keys_to_insert:
        bplus_tree.insert(key)

    print("Inorder Traversal:", bplus_tree.inorder_traversal())

    search_key = 15
    """if bplus_tree.search(search_key):
        print(f"{search_key} found in the B+ tree.")
    else:
        print(f"{search_key} not found in the B+ tree.")"""
    print(bplus_tree.searchkey(search_key))

    bplus_tree.print_leaf_keys()
