import math

class Node:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.parent = None
        self.check_leaf = False
    
    def insert_at_leaf(self, value, key):
        if self.values:
            temp1 = self.values
            for i in range(len(temp1)):
                if value == temp1[i]:
                    self.keys[i].append(key)
                    break
                elif value < temp1[i]:
                    self.values = self.values[:i] + [value] + self.values[i:]
                    self.keys = self.keys[:i] + [[key]] + self.keys[i:]
                elif (i + 1) == len(temp1):
                    self.values.append(value)
                    self.keys.append([key])
                    break
        else:
            self.values = [value]
            self.keys = [[key]]
    
    def __repr__(self):
        return f"{str(self.values)}, {str(self.keys)}"

class BPlusTree:
    def __init__(self, order):
        self.root = Node(order=order)
        self.root.check_leaf = True
    
    def insert(self, value, key):
        old_node = self.search(value)
        old_node.insert_at_leaf(value, key)

        if len(old_node.values) == old_node.order:
            node1 = Node(order=old_node.order)
            node1.check_leaf = True
            node1.parent = old_node.parent

            mid = int(math.ceil(old_node.order / 2)) - 1

            node1.values = old_node.values[mid + 1:]
            node1.keys = old_node.keys[mid + 1:]

            old_node.values = old_node.values[:mid + 1]
            old_node.keys = old_node.keys[:mid + 1]

            self.insert_at_parent(old_node, node1.values[0], node1)
        
    def insert_at_parent(self, n, value, ndash):
        if self.root == n:
            rootNode = Node(n.order)
            rootNode.values = [value]
            rootNode.keys = [n, ndash]
            self.root = rootNode
            n.parent = rootNode
            ndash.parent = rootNode
            return self.root

        parentNode = n.parent
        temp3 = parentNode.keys

        for i in range(len(temp3)):
            if temp3[i] == n:
                parentNode.values = parentNode.values[:i] + [value] + parentNode.values[i:]
                parentNode.keys = parentNode.keys[:i+1] + [ndash] + parentNode.keys[i+1:]

                if len(parentNode.keys) > parentNode.order:
                    parentdash = Node(parentNode.order)
                    parentdash.parent = parentNode.parent
                    
                    mid = int(math.ceil(parentNode.order/2)) - 1

                    parentdash.values = parentNode.values[mid + 1:]
                    parentdash.keys = parentNode.keys[mid + 1:]
                    value_ = parentNode.values[mid]

                    if mid == 0:
                        parentNode.values = parentNode.values[:mid + 1]
                    else:
                        parentNode.values = parentNode.values[:mid]
                    
                    parentNode.keys = parentNode.keys[:mid + 1]

                    for j in parentNode.keys:
                        j.parent = parentNode
                
                    for j in parentdash.keys:
                        j.parent = parentdash
                    
                    self.insert_at_parent(parentNode, value_, parentdash)


    def search(self, search_elt):
        current_node = self.root

        while current_node.check_leaf is False:
            temp2 = current_node.values
            for i in range(len(temp2)):
                if search_elt == temp2[i]:
                    current_node = current_node.keys[i + 1]
                    break
                elif search_elt < temp2[i]:
                    current_node = current_node.keys[i]
                    break
                elif (i + 1) == len(current_node.values):
                    current_node = current_node.keys[i + 1]
                    break
        return current_node
    
def display(tree):
    lst = [tree.root]
    level = [0]
    leaf = None
    flag = 0
    lev_leaf = 0

    node1 = Node(str(level[0]) + str(tree.root.values))

    while len(lst) != 0:
        x = lst.pop(0)
        lev = level.pop(0)
        if (x.check_leaf is False):
            for i, item in enumerate(x.keys):
                print(item.values)
        else:
            for i, item in enumerate(x.keys):
                print(item.values)
            
            if flag == 0:
                lev_leaf = lev
                leaf = x
                flag = 1


record_len = 3
bplustree = BPlusTree(record_len)
bplustree.insert(5, 33)
bplustree.insert(15, 21)
bplustree.insert(25, 31)
bplustree.insert(35, 41)
bplustree.insert(45, 51)
bplustree.insert(55, 61)


# display(bplustree)
bplustree.print_tree()
print(bplustree.root.values)
print(bplustree.root.keys[0].values)
print(bplustree.root.keys[1].values)
print(bplustree.root.keys[2].values)
# print(bplustree.root.keys)
        
