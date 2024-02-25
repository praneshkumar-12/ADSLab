class Node:
    """
    Node class for a Binary Tree.

    Attributes:
    - item: The value stored in the node.
    - left: Reference to the left child node.
    - right: Reference to the right child node.
    - parent: Reference to the parent node.
    """

    def __init__(self, item=None, left=None, right=None, parent=None):
        """
        Initializes a Node with the given item and optional left, right, and parent references.

        Parameters:
        - item: The value to be stored in the node (default is None).
        - left: Reference to the left child node (default is None).
        - right: Reference to the right child node (default is None).
        - parent: Reference to the parent node (default is None).
        """
        self.item = item      # Value stored in the node
        self.left = left      # Reference to the left child node
        self.right = right    # Reference to the right child node
        self.parent = parent  # Reference to the parent node
