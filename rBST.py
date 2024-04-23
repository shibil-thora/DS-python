class Node: 
    def __init__(self, value): 
        self.value = value
        self.right = None 
        self.left = None 

    def __str__(self): 
        return f'{self.left.value if self.left else None}<--({self.value})-->{self.right.value if self.right else None}'

class BinaryTree(): 
    def __init__(self): 
        self.root = None 

    def min_value(self, current_node): 
        while current_node.left is not None: 
            current_node = current_node.left 
        return current_node.value

    def __r_insert(self, current_node, value): 
        if current_node == None: 
            return Node(value)
        if value < current_node.value: 
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value: 
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def insert(self, value): 
        if self.root == None: 
            self.root = Node(value)
            return True
        self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value): 
        if current_node == None: 
            return False 
        if value == current_node.value: 
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value: 
            return self.__r_contains(current_node.right, value)
        
    def contains(self, value): 
        return self.__r_contains(self.root, value)
    
    def __delete_node(self, current_node, value): 
        if current_node == None: 
            return None
        if value < current_node.value: 
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value: 
            current_node.right = self.__delete_node(current_node.right, value)
        else: 
            if current_node.left == None and current_node.right == None: 
                return None 
            elif current_node.left == None: 
                current_node = current_node.right
            elif current_node.right == None: 
                current_node = current_node.left
            else: 
                sub_tree_min = self.min_value(current_node.right) 
                current_node.value = sub_tree_min 
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
            
        return current_node

    def delete_node(self, value): 
        self.__delete_node(self.root, value)


tree = BinaryTree()
# [tree.insert(i) for i in [47, 76, 52, 82, 21, 18, 27, 5, 19, 25, 35, 50, 60, 77, 90]]
[tree.insert(i) for i in [3, 2, 5]]
tree.delete_node(3)
print(tree.root)