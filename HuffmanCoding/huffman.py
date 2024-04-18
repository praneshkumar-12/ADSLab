# Importing the heapq module for heap operations
import heapq

# Initializing an empty heap
heap = []
heapq.heapify(heap)

# Dictionary to store the Huffmann codes for each character
huffmann_code = {}


# Node class representing a node in the binary tree
class Node:
    def __init__(self, char, count, parent=None, left=None, right=None):
        # Character stored at the node
        self.char = char
        # Frequency of the character
        self.count = count
        # References to parent, left, and right nodes
        self.parent = parent
        self.left = left
        self.right = right


# BinaryTree class representing a binary tree
class BinaryTree:
    def __init__(self, root=None, left=None, right=None):
        # Root node of the tree
        self.root = root

        # Establishing parent-child relationships
        if left:
            left.parent = self.root
            self.root.left = left.root
            left.root = None

        if right:
            right.parent = self.root
            self.root.right = right.root
            right.root = None

    # Comparison method to facilitate heap operations
    def __lt__(self, other):
        if self.root.count < other.root.count:
            return True
        return False


# Function to calculate the frequency of each character in a given string
def calculate_frequency(string):
    freq = {}
    # Iterate through the string and count the occurrences of each character
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


# Function to construct a heap of binary trees from the frequency dictionary
def construct_heap(frequencies):
    for char, count in frequencies.items():
        # Create a binary tree for each character with its frequency
        tree = BinaryTree(root=Node(char, count))
        # Push the tree into the heap
        heapq.heappush(heap, tree)


# Function to construct the Huffmann coding tree from the heap
def construct_huffmann_coding_tree():
    # While there is more than one tree in the heap
    while len(heap) != 1:
        # Pop the two trees with the smallest frequencies
        first_smallest = heapq.heappop(heap)
        second_smallest = heapq.heappop(heap)

        # Create a new binary tree with the sum of the frequencies
        temp = BinaryTree(
            root=Node(
                char=None, count=first_smallest.root.count + second_smallest.root.count
            ),
            left=first_smallest,
            right=second_smallest,
        )

        # Push the new tree back into the heap
        heapq.heappush(heap, temp)


# Recursive function to generate the Huffmann code table from the tree
def generate_huffmann_table(huffmann_tree_node, current_code=""):
    # Base case: if the node is a leaf node (no left or right children)
    if huffmann_tree_node.left is None and huffmann_tree_node.right is None:
        char = huffmann_tree_node.char
        code = current_code

        # Store the Huffmann code for the character in the dictionary
        huffmann_code[char] = code
    else:
        # Recursively generate codes for left and right children
        generate_huffmann_table(huffmann_tree_node.left, str(current_code) + "0")
        generate_huffmann_table(huffmann_tree_node.right, str(current_code) + "1")


# Function to generate the encoded string using the Huffmann code table
def generate_huffmann_code(string):
    code = ""
    # Iterate through the string and encode each character
    for ch in string:
        code += huffmann_code[ch]

    return code


# Main function
if __name__ == "__main__":
    # Prompting the user for input
    string = input("Enter the string to find the Huffmann coding: ")

    # Calculating frequencies of characters in the input string
    frequencies = calculate_frequency(string)
    # Constructing a heap of binary trees
    construct_heap(frequencies)
    # Constructing the Huffmann coding tree
    construct_huffmann_coding_tree()
    # Generating the Huffmann code table
    generate_huffmann_table(heap[0].root)

    # Generating the encoded string using the Huffmann code table
    encoded_string = generate_huffmann_code(string)

    # Displaying the Huffmann code table
    print("\nHuffmann Code Table:")
    print(huffmann_code)

    # Displaying the Huffmann encoded string
    print(f"\nHuffmann Code for {string}:")
    print(encoded_string)
