from Node import Node  # Importing the Node class from the Node module


class BST:
    """
    Binary Search Tree (BST) class.
    """

    def __init__(self, item=None, t_left=None, t_right=None):
        """
        Initializes the Binary Search Tree.

        Parameters:
        - item: Item to be inserted as the root of the BST (optional).
        - t_left: Left subtree of the BST (optional).
        - t_right: Right subtree of the BST (optional).
        """
        self.root = None  # Initialize the root node
        self.size = 0  # Initialize the size of the BST
        self.res = ""  # Initialize an empty string for storing traversal results

        # If item is provided during initialization, add it as the root
        if item is not None:
            self.root = self.addRoot(item)

        # If a left subtree is provided, attach it to the left of the root
        if t_left is not None:
            if self.root is None:
                raise ValueError("Root is empty!")
            elif t_left.root is not None:
                self.root.left = t_left.root
                t_left.parent = self.root
                t_left.root = None
                self.size += t_left.size

        # If a right subtree is provided, attach it to the right of the root
        if t_right is not None:
            if self.root is None:
                raise ValueError("Root is empty!")
            elif t_right.root is not None:
                self.root.right = t_right.root
                t_right.parent = self.root
                t_right.root = None
                self.size += t_right.size

    def isEmpty(self):
        """
        Checks if the BST is empty.

        Returns:
        - True if the BST is empty, False otherwise.
        """
        return True if self.root is None else False  # Check if the BST is empty

    def addRoot(self, item):
        """
        Adds a root node to the BST.

        Parameters:
        - item: Item to be inserted as the root.

        Returns:
        - The newly added root node.
        """
        if self.root is not None:
            raise ValueError("Root already exists!")
        self.root = Node(item=item)  # Create a new root node with the provided item
        self.size += 1  # Increase the size of the BST
        return self.root

    def __len__(self):
        """
        Returns the size of the BST.

        Returns:
        - The size of the BST.
        """
        return self.size  # Return the size of the BST

    def addLeft(self, item, pos):
        """
        Adds a left child to the specified position in the BST.

        Parameters:
        - item: Item to be inserted as the left child.
        - pos: Position where the left child should be inserted.

        Returns:
        - The newly added left child node.
        """
        if pos.left is not None:
            return ValueError("Left child already exists!")

        pos.left = Node(
            item=item, parent=pos
        )  # Create a new node and attach it to the left of the given position
        self.size += 1  # Increase the size of the BST
        return pos.left

    def addRight(self, item, pos):
        """
        Adds a right child to the specified position in the BST.

        Parameters:
        - item: Item to be inserted as the right child.
        - pos: Position where the right child should be inserted.

        Returns:
        - The newly added right child node.
        """
        if pos.right is not None:
            return ValueError("Right child already exists!")

        pos.right = Node(
            item=item, parent=pos
        )  # Create a new node and attach it to the right of the given position
        self.size += 1  # Increase the size of the BST
        return pos.right

    def insert(self, item, pos=None):
        """
        Inserts an item into the BST.

        Parameters:
        - item: Item to be inserted.
        - pos: Position where the item should be inserted (optional).
               If not provided, item is inserted at the root.

        Returns:
        - None.
        """
        if pos is None:
            if self.isEmpty():
                self.addRoot(item)  # If the BST is empty, add the item as the root
                return self.root
            else:
                pos = self.root

        if item < pos.item:
            if pos.left is None:
                self.addLeft(
                    item, pos
                )  # If item is less than current position, recursively insert it to the left
            else:
                self.insert(item, pos.left)

        if item > pos.item:
            if pos.right is None:
                self.addRight(
                    item, pos
                )  # If item is greater than current position, recursively insert it to the right
            else:
                self.insert(item, pos.right)

        if item == pos.item:
            return None  # If item already exists in the BST, do nothing

    def _preorder(self, pos):
        """
        Helper method for performing preorder traversal recursively.

        Parameters:
        - pos: Current position/node.

        Returns:
        - None.
        """
        self.res += (
            str(pos.item) + " "
        )  # Append the item of the current position to the result string

        if pos.left is not None:
            self._preorder(pos.left)  # Recursively traverse the left subtree

        if pos.right is not None:
            self._preorder(pos.right)  # Recursively traverse the right subtree

    def preorder(self, pos):
        """
        Performs preorder traversal of the BST.

        Parameters:
        - pos: Starting position/node.

        Returns:
        - Preorder traversal result.
        """
        self._preorder(pos)
        temp = self.res
        self.res = ""
        return temp  # Return the preorder traversal result

    def _inorder(self, pos):
        """
        Helper method for performing inorder traversal recursively.

        Parameters:
        - pos: Current position/node.

        Returns:
        - None.
        """
        if pos.left is not None:
            self._inorder(pos.left)

        self.res += str(pos.item) + " "

        if pos.right is not None:
            self._inorder(pos.right)

    def inorder(self, pos):
        """
        Performs inorder traversal of the BST.

        Parameters:
        - pos: Starting position/node.

        Returns:
        - Inorder traversal result.
        """
        self._inorder(pos)
        temp = self.res
        self.res = ""
        return temp  # Return the inorder traversal result

    def _postorder(self, pos):
        """
        Helper method for performing postorder traversal recursively.

        Parameters:
        - pos: Current position/node.

        Returns:
        - None.
        """
        if pos.left is not None:
            self._postorder(pos.left)

        if pos.right is not None:
            self._postorder(pos.right)

        self.res += str(pos.item) + " "

    def postorder(self, pos):
        """
        Performs postorder traversal of the BST.

        Parameters:
        - pos: Starting position/node.

        Returns:
        - Postorder traversal result.
        """
        self._postorder(pos)
        temp = self.res
        self.res = ""
        return temp  # Return the postorder traversal result

    def search(self, item, pos=None):
        """
        Searches for an item in the BST.

        Parameters:
        - item: Item to be searched.
        - pos: Starting position/node (optional).

        Returns:
        - Node containing the item if found, None otherwise.
        """
        if pos is None:
            pos = self.root
        if pos.item == item:
            return pos

        elif item < pos.item and pos.left is not None:
            return self.search(item, pos.left)

        elif item > pos.item and pos.right is not None:
            return self.search(item, pos.right)

        return None

    def findMin(self, pos=None):
        """
        Finds the minimum value node in the BST.

        Parameters:
        - pos: Starting position/node (optional).

        Returns:
        - Node containing the minimum value.
        """
        if pos is None:
            pos = self.root
        if pos.left is not None:
            return self.findMin(pos.left)
        if pos.left is None:
            return pos

    def delete(self, item, position=None):
        """
        Deletes an item from the BST.

        Parameters:
        - item: Item to be deleted.
        - position: Starting position/node (optional).

        Returns:
        - None.
        """
        if position is None:
            position = self.root

        pos = self.search(item, position)
        if pos is None:
            raise ValueError("No such value in tree!")

        parent = pos.parent

        if pos.left is None and pos.right is None:
            if parent is None:
                self.root = None
            elif parent.left == pos:
                parent.left = None
                pos.parent = None
                del pos
            else:
                parent.right = None
                pos.parent = None
                del pos
        elif pos.left is not None and pos.right is None:
            if parent is None:
                self.root = pos.left
                pos.parent.left = None
                self.root.parent = None
                del pos
            elif parent.left == pos:
                parent.left = None
                pos.left = parent.left
                pos.parent = None
                pos.left = None
                parent.left.parent = parent
                del pos
            else:
                parent.right = None
                pos.left = parent.right
                pos.parent = None
                pos.left = None
                parent.right.parent = parent
                del pos
        elif pos.right is not None and pos.left is None:
            if parent is None:
                self.root = pos.right
                pos.parent.right = None
                self.root.parent = None
                del pos
            elif parent.left == pos:
                parent.left = None
                pos.right = parent.left
                pos.parent = None
                pos.right = None
                parent.left.parent = parent
                del pos
            else:
                parent.right = None
                pos.right = parent.right
                pos.parent = None
                pos.right = None
                parent.right.parent = parent
                del pos
        else:
            smallest_node = self.findMin(pos.right)
            pos.item = smallest_node.item
            self.delete(smallest_node.item, pos.right)

        self.size -= 1


if __name__ == "__main__":
    # Create a BST instance
    bst = BST()

    # Insert elements into the BST
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    # Perform preorder traversal and print the result
    print("Preorder traversal:", bst.preorder(bst.root))

    # Perform inorder traversal and print the result
    print("Inorder traversal:", bst.inorder(bst.root))

    # Perform postorder traversal and print the result
    print("Postorder traversal:", bst.postorder(bst.root))

    # Search for an element in the BST
    search_item = 15
    search_result = bst.search(search_item)
    if search_result:
        print(f"{search_item} found in the BST.")
    else:
        print(f"{search_item} not found in the BST.")

    # Delete an element from the BST
    delete_item = 10
    bst.delete(delete_item)
    print(f"Deleted {delete_item} from the BST.")

    # Perform inorder traversal after deletion and print the result
    print("Inorder traversal after deletion:", bst.inorder(bst.root))
