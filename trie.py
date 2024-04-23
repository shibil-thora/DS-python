class Node:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
    
    def __str__(self): 
        return f'[{self.char} -{tuple(self.children.keys())}]'
    

class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word): 
        temp = self.root 
        for char in word: 
            if char in temp.children: 
                temp = temp.children[char]
            else: 
                node = Node(char)
                temp.children[char] = node 
                temp = node 
        temp.is_end = True

    def search(self, word): 
        temp = self.root
        for char in word: 
            if char in temp.children: 
                temp = temp.children[char]
            else: 
                return False 
        return temp.is_end

    def autocomplete(self, word):
        result = []
        temp = self.root
        for char in word:           
            if char in temp.children:
                temp = temp.children[char]
            else:
                return []
        self.helper(temp, result, word[:-1]) 
        return result
 
    def helper(self, current, result, prefix):
        if current.is_end:
            result.append(prefix + current.char)       
        for child in current.children.values():
            self.helper(child, result, prefix + current.char) 


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert('app')
print(trie.search("apple"))  # Returns True
print(trie.search("app"))    # Returns False

trie.insert('apple')
trie.insert('app')
trie.insert('approach')
print(trie.autocomplete('app'))
print(trie.root.children)
