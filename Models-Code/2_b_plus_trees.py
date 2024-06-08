class Node:
    def __init__(self, leaf=False):
        self.keys = []  # List to store keys
        self.values = []  # List to store values
        self.leaf = leaf  # Boolean flag to indicate if the node is a leaf
        self.next = None  # Reference to the next node


class BPlusTree:
    def __init__(self, degree):
        self.root = Node(leaf=True)  # Create the root node as a leaf node
        self.degree = degree  # Degree of the B+ tree

    # Search for a key in the B+ tree
    def search(self, key):
        curr = self.root
        while not curr.leaf:
            i = 0
            while i < len(curr.keys):
                if key < curr.keys[i]:
                    break
                i += 1
            curr = curr.values[i]
        i = 0
        while i < len(curr.keys):
            if curr.keys[i] == key:
                return True
            i += 1
        return False

    # Insert a key into the B+ tree
    def insert(self, key):
        curr = self.root
        if len(curr.keys) == 2 * self.degree:  # If the root is full, split it
            new_root = Node()  # Create a new root node
            self.root = new_root
            new_root.values.append(curr)  # Make the old root a child of the new root
            self.split(new_root, 0, curr)  # Split the old root and move its keys and values to the new root
            self.insert_non_full(new_root, key)  # Insert the key into the new root
        else:
            self.insert_non_full(curr, key)  # Insert the key into the non-full root or leaf node

    # Insert a key into a non-full node
    def insert_non_full(self, curr, key):
        i = 0
        while i < len(curr.keys):
            if key < curr.keys[i]:
                break
            i += 1
        if curr.leaf:
            curr.keys.insert(i, key)  # Insert the key into the leaf node
        else:
            if len(curr.values[i].keys) == 2 * self.degree:  # If the child is full, split it
                self.split(curr, i, curr.values[i])  # Split the child node
                if key > curr.keys[i]:  # Determine which child to insert the key into
                    i += 1
            self.insert_non_full(curr.values[i], key)  # Recursively insert the key into the child node

    # Split a node into two nodes
    def split(self, parent, i, node):
        new_node = Node(leaf=node.leaf)  # Create a new node with the same leaf status as the original node
        parent.values.insert(i + 1, new_node)  # Insert the new node into the parent's values list
        parent.keys.insert(i, node.keys[self.degree - 1])  # Move the median key to the parent node
        new_node.keys = node.keys[self.degree:]  # Move the keys greater than the median to the new node
        node.keys = node.keys[:self.degree - 1]  # Update the original node's keys to contain the keys less than the median
        if not new_node.leaf:
            new_node.values = node.values[self.degree:]  # Move the values greater than the median to the new node
            node.values = node.values[:self.degree]  # Update the original node's values to contain the values less than the median

    # Steal a key from the left sibling
    def steal_from_left(self, parent, i):
        node = parent.values[i]
        left_sibling = parent.values[i - 1]
        node.keys.insert(0, parent.keys[i - 1])  # Move the key from the parent to the node
        parent.keys[i - 1] = left_sibling.keys.pop(-1)  # Move the rightmost key from the left sibling to the parent
        if not node.leaf:
            node.values.insert(0, left_sibling.values.pop(-1))  # Move the rightmost value from the left sibling to the node

    # Steal a key from the right sibling
    def steal_from_right(self, parent, i):
        node = parent.values[i]
        right_sibling = parent.values[i + 1]
        node.keys.append(parent.keys[i])  # Move the key from the parent to the node
        parent.keys[i] = right_sibling.keys.pop(0)  # Move the leftmost key from the right sibling to the parent
        if not node.leaf:
            node.values.append(right_sibling.values.pop(0))  # Move the leftmost value from the right sibling to the node

    # Delete a key from the B+ tree
    def delete(self, key):
        curr = self.root
        found = False
        i = 0
        while i < len(curr.keys):
            if key == curr.keys[i]:
                found = True
                break
            elif key < curr.keys[i]:
                break
            i += 1
        if found:
            if curr.leaf:
                curr.keys.pop(i)  # Remove the key from the leaf node
            else:
                pred = curr.values[i]  # Get the predecessor node
                if len(pred.keys) >= self.degree:  # If the predecessor has enough keys, replace the key with the predecessor's maximum key
                    pred_key = self.get_max_key(pred)
                    curr.keys[i] = pred_key
                    self.delete_from_leaf(pred_key, pred)  # Delete the predecessor's maximum key from the predecessor
                else:
                    succ = curr.values[i + 1]  # Get the successor node
                    if len(succ.keys) >= self.degree:  # If the successor has enough keys, replace the key with the successor's minimum key
                        succ_key = self.get_min_key(succ)
                        curr.keys[i] = succ_key
                        self.delete_from_leaf(succ_key, succ)  # Delete the successor's minimum key from the successor
                    else:
                        self.merge(curr, i, pred, succ)  # Merge the node with its predecessor and successor
                        self.delete_from_leaf(key, pred)  # Delete the key from the predecessor
            if curr == self.root and not curr.keys:  # If the root becomes empty, update the root
                self.root = curr.values[0]
        else:
            if curr.leaf:
                return False
            else:
                if len(curr.values[i].keys) < self.degree:  # If the child has less than the minimum number of keys
                    if i != 0 and len(curr.values[i - 1].keys) >= self.degree:  # Try to steal a key from the left sibling
                        self.steal_from_left(curr, i)
                    elif i != len(curr.keys) and len(curr.values[i + 1].keys) >= self.degree:  # Try to steal a key from the right sibling
                        self.steal_from_right(curr, i)
                    else:
                        if i == len(curr.keys):
                            i -= 1
                        self.merge(curr, i, curr.values[i], curr.values[i + 1])  # Merge the child with its left sibling or right sibling
                self.delete(key)  # Recursively delete the key from the child node

    # Delete a key from a leaf node
    def delete_from_leaf(self, key, leaf):
        leaf.keys.remove(key)  # Remove the key from the leaf node
        if leaf == self.root or len(leaf.keys) >= self.degree // 2:  # If the leaf node is the root or has enough keys, no further action is needed
            return
        parent = self.find_parent(leaf)  # Find the parent node of the leaf node
        i = parent.values.index(leaf)  # Find the index of the leaf node in the parent's values list
        if i > 0 and len(parent.values[i - 1].keys) > self.degree // 2:  # Try to rotate right with the left sibling
            self.rotate_right(parent, i)
        elif i < len(parent.keys) and len(parent.values[i + 1].keys) > self.degree // 2:  # Try to rotate left with the right sibling
            self.rotate_left(parent, i)
        else:
            if i == len(parent.keys):
                i -= 1
            self.merge(parent, i, parent.values[i], parent.values[i + 1])  # Merge the leaf node with its left sibling or right sibling

    # Get the minimum key in a node
    def get_min_key(self, node):
        while not node.leaf:
            node = node.values[0]
        return node.keys[0]

    # Get the maximum key in a node
    def get_max_key(self, node):
        while not node.leaf:
            node = node.values[-1]
        return node.keys[-1]

    # Merge two nodes
    def merge(self, parent, i, pred, succ):
        pred.keys += succ.keys  # Move the keys from the successor to the predecessor
        pred.values += succ.values  # Move the values from the successor to the predecessor
        parent.values.pop(i + 1)  # Remove the successor from the parent's values list
        parent.keys.pop(i)  # Remove the key between the predecessor and the successor
        if parent == self.root and not parent.keys:  # If the root becomes empty, update the root
            self.root = pred

    # Fix the tree after deletion
    def fix(self, parent, i):
        node = parent.values[i]
        if i > 0 and len(parent.values[i - 1].keys) >= self.degree:  # Try to rotate right with the left sibling
            self.rotate_right(parent, i)
        elif i < len(parent.keys) and len(parent.values[i + 1].keys) >= self.degree:  # Try to rotate left with the right sibling
            self.rotate_left(parent, i)
        else:
            if i == len(parent.keys):
                i -= 1
            self.merge(parent, i, node, parent.values[i + 1])  # Merge the node with its left sibling or right sibling

    # Rotate a node to the right
    def rotate_right(self, parent, i):
        node = parent.values[i]
        prev = parent.values[i - 1]
        node.keys.insert(0, parent.keys[i - 1])  # Move the key from the parent to the node
        parent.keys[i - 1] = prev.keys.pop(-1)  # Move the rightmost key from the left sibling to the parent
        if not node.leaf:
            node.values.insert(0, prev.values.pop(-1))  # Move the rightmost value from the left sibling to the node

    # Rotate a node to the left
    def rotate_left(self, parent, i):
        node = parent.values[i]
        next = parent.values[i + 1]
        node.keys.append(parent.keys[i])  # Move the key from the parent to the node
        parent.keys[i] = next.keys.pop(0)  # Move the leftmost key from the right sibling to the parent
        if not node.leaf:
            node.values.append(next.values.pop(0))  # Move the leftmost value from the right sibling to the node

    # Print the B+ tree
    def print_tree(self):
        curr_level = [self.root]
        while curr_level:
            next_level = []
            for node in curr_level:
                print(str(node.keys), end=" ")  # Print the keys in the current level
                if not node.leaf:
                    next_level += node.values  # Add the child nodes to the next level
            print()
            curr_level = next_level


if __name__ == "__main__":
    # Create a B+ tree with degree 3
    tree = BPlusTree(3)

    # Insert some keys
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)

    # Print the tree
    tree.print_tree()

    # Delete a key
    # tree.delete(3)

    # # Print the tree
    # tree.print_tree()
