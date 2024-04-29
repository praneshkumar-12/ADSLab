import heapq

heap = []
heapq.heapify(heap)

huffmann_code = {}

class Node:
    def __init__(self, char, count, parent=None, left=None, right=None):
        self.char = char
        self.count = count
        self.parent = parent
        self.left = left
        self.right = right



class BinaryTree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root

        if left:
            left.parent = self.root
            self.root.left = left.root
            left.root = None

        if right:
            right.parent = self.root
            self.root.right = right.root
            right.root = None

    def __lt__(self, other):
        if self.root.count < other.root.count:
            return True
        return False


def calculate_frequency(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


def construct_heap(frequencies):
    for char, count in frequencies.items():
        tree = BinaryTree(root=Node(char, count))
        heapq.heappush(heap, tree)


def construct_huffmann_coding_tree():
    while len(heap) != 1:
        first_smallest = heapq.heappop(heap)
        second_smallest = heapq.heappop(heap)

        temp = BinaryTree(
            root=Node(
                char=None, count=first_smallest.root.count + second_smallest.root.count
            ),
            left=first_smallest,
            right=second_smallest,
        )

        heapq.heappush(heap, temp)


def generate_huffmann_table(huffmann_tree_node, current_code=""):
    if huffmann_tree_node.left is None and huffmann_tree_node.right is None:
        char = huffmann_tree_node.char
        code = current_code

        huffmann_code[char] = code
    else:
        generate_huffmann_table(huffmann_tree_node.left, str(current_code) + "0")
        generate_huffmann_table(huffmann_tree_node.right, str(current_code) + "1")


def generate_huffmann_code(string):
    code = ""
    for ch in string:
        code += huffmann_code[ch]

    return code


if __name__ == "__main__":
    string = input("Enter the string to find the Huffmann coding: ")

    frequencies = calculate_frequency(string)
    construct_heap(frequencies)
    construct_huffmann_coding_tree()
    generate_huffmann_table(heap[0].root)

    encoded_string = generate_huffmann_code(string)

    print("\nHuffmann Code Table:")
    print(huffmann_code)

    print(f'\nHuffmann Code for "{string}":')
    print(encoded_string)
