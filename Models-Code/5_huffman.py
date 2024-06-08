import heapq

# Create an empty heap
heap = []
heapq.heapify(heap)

# Create an empty dictionary to store Huffman codes
huffmann_code = {}

# Define a Node class to represent a node in the Huffman coding tree
class Node:
    def __init__(self, char, count, parent=None, left=None, right=None):
        self.char = char
        self.count = count
        self.parent = parent
        self.left = left
        self.right = right

# Define a BinaryTree class to represent a binary tree
class BinaryTree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root

        # If left child is provided, set its parent and attach it to the root
        if left:
            left.parent = self.root
            self.root.left = left.root
            left.root = None

        # If right child is provided, set its parent and attach it to the root
        if right:
            right.parent = self.root
            self.root.right = right.root
            right.root = None

    # Define the less than operator for comparing two BinaryTree objects based on their root node counts
    def __lt__(self, other):
        if self.root.count < other.root.count:
            return True
        return False

# Function to calculate the frequency of each character in the input string
def calculate_frequency(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

# Function to construct the initial heap from the character frequencies
def construct_heap(frequencies):
    for char, count in frequencies.items():
        # Create a BinaryTree object with a Node containing the character and its count
        tree = BinaryTree(root=Node(char, count))
        # Push the BinaryTree object into the heap
        heapq.heappush(heap, tree)

# Function to construct the Huffman coding tree
def construct_huffman_coding_tree():
    while len(heap) != 1:
        # Pop the two smallest trees from the heap
        first_smallest = heapq.heappop(heap)
        second_smallest = heapq.heappop(heap)

        # Create a new tree with a Node containing the sum of counts of the two smallest trees
        temp = BinaryTree(
            root=Node(
                char=None, count=first_smallest.root.count + second_smallest.root.count
            ),
            left=first_smallest,
            right=second_smallest,
        )

        # Push the new tree back into the heap
        heapq.heappush(heap, temp)

# Function to generate the Huffman code table
def generate_huffman_table(huffman_tree_node, current_code=""):
    if huffman_tree_node.left is None and huffman_tree_node.right is None:
        # If the node is a leaf node, store its character and the current code in the Huffman code table
        char = huffman_tree_node.char
        code = current_code

        huffmann_code[char] = code
    else:
        # Recursively generate the Huffman code table for the left and right subtrees
        generate_huffman_table(huffman_tree_node.left, str(current_code) + "0")
        generate_huffman_table(huffman_tree_node.right, str(current_code) + "1")

# Function to generate the Huffman code for the input string
def generate_huffman_code(string):
    code = ""
    for ch in string:
        # Concatenate the Huffman code for each character in the input string
        code += huffmann_code[ch]

    return code

# Main program
if __name__ == "__main__":
    # Prompt the user to enter the string to find the Huffman coding
    string = input("Enter the string to find the Huffman coding: ")

    # Calculate the frequency of each character in the string
    frequencies = calculate_frequency(string)

    # Construct the initial heap from the character frequencies
    construct_heap(frequencies)

    # Construct the Huffman coding tree
    construct_huffman_coding_tree()

    # Generate the Huffman code table
    generate_huffman_table(heap[0].root)

    # Generate the Huffman code for the input string
    encoded_string = generate_huffman_code(string)

    # Print the Huffman code table
    print("\nHuffman Code Table:")
    print(huffmann_code)

    # Print the Huffman code for the input string
    print(f'\nHuffman Code for "{string}":')
    print(encoded_string)
