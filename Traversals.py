from rBST import Node

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

    def BFS(self): 
        current_node = self.root 
        queue = []  # Using a List for queue is not efficient But for understanding purposes.
        result = []
        queue.append(current_node)
        while len(queue): 
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None: 
                queue.append(current_node.left)
            if current_node.right is not None: 
                queue.append(current_node.right)
        return result
    
    def dfs_pre_order(self): 
        result = []
        def traverse(current): 
            result.append(current.value)
            if current.left is not None: 
                traverse(current.left)
            if current.right is not None: 
                traverse(current.right) 
        traverse(self.root)
        return result 
            
    def dfs_post_order(self): 
        result = []
        def traverse(current): 
            if current.left is not None: 
                traverse(current.left)
            if current.right is not None: 
                traverse(current.right) 
            result.append(current.value) 
        traverse(self.root)
        return result

    def dfs_in_order(self): 
        result = []
        def traverse(current): 
            if current.left: 
                traverse(current.left)
            result.append(current.value)
            if current.right: 
                traverse(current.right)
        traverse(self.root)
        return result
            
            


tree = BinaryTree()
[tree.insert(i) for i in [47, 21, 76, 52, 82, 18, 27]]
print(tree.dfs_in_order())