class NodeSll: 
    def __init__(self, value): 
        self.value = value
        self.next = None

    def __str__(self):
        return f'<SLL-Node: {self.value}>'

class NodeDll:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f'<DLL-Node: {self.value}>'


#------------------------------SINGLY---------------------------------#
class SinklyLinkedList:
    def __init__(self, value):
        node = NodeSll(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        i = 0
        while temp:
            print(f'{i}:', temp.value)
            temp = temp.next
            i += 1

    def append(self, value):
        node = NodeSll(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else: 
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        if self.length == 0: 
            return None
        temp = self.tail
        if self.length == 1: 
            self.head = None
            self.tail = None
        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def prepend(self, value): 
        node = NodeSll(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else: 
            node.next = self.head
            self.head = node
        self.length += 1
        return True
    
    # def pop_first(self):
    #     if self.length == 0: 
    #         return None
    #     temp = self.head
    #     if self.length == 1: 
    #         self.head = None
    #         self.tail = None
    #     else: 
    #         temp

    def set_value(self, index, value): 
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True
        else: 
            return False

    def insert(self, index, value): 
        if index < 0 or index > self.length: 
            return None
        if index == 0: 
            return self.prepend(value)
        if index == self.length: 
            return self.append(value)
        node = NodeSll(value)
        temp = self.get(index-1)
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next 
        temp.next = None
        self.length -= 1
        return temp
    
    def remove_dups(self): 
        temp = self.head
        i = 0
        while temp and temp.next: 
            if temp.value == temp.next.value: 
                temp = temp.next
                self.remove(i)
            else:
                temp = temp.next
            i += 1
    
    def partition_list(self, x):
        
        pass

    def get_by_value(self, value): 
        temp = self.head
        while temp: 
            if temp.value == value: 
                return temp
            temp = temp.next
        return None
    
    def remove_by_value(self, value): 
        if self.head == None: 
            return None
        temp = self.head
        if self.head.value == value: 
            self.head = self.head.next
            temp.next = None
            return temp
        else: 
            pre = None
            while temp: 
                if temp.value == value:
                    pre.next = temp.next
                    temp.next = None
                    return temp
                pre = temp
                temp = temp.next

    
            


#------------------------------DOUBLY---------------------------------#
class DoublyLinkedList:
    def __init__(self, value):
        node = NodeDll(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        i = 0
        while temp:
            print(f'{i}:', temp.value)
            temp = temp.next
            i += 1


    def append(self, value):
        node = NodeDll(value)
        if self.length == 0:
            self.head = node
            self.tail = node    
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length += 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length // 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def prepend(self, value): 
        node = NodeDll(value)
        if self.length == 0: 
            self.head = node
            self.tail = node 
        else: 
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def set_value(self, index, value): 
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True 
        return False
    
    def insert(self, index, value): 
        if index < 0 or index > self.length: 
            return None
        if index == 0: 
            return self.prepend(value)
        if index == self.length: 
            return self.append(value)
        node = NodeDll(value)
        temp = self.get(index-1)
        node.next = temp.next
        node.next.prev = node
        temp.next = node
        node.prev = temp
        self.length += 1
        return True
    
        
        

dll = DoublyLinkedList(1)
sll = SinklyLinkedList(1)
for i in [2, 3, 5, 6, 2, 7, 8]:
    dll.append(i)
    sll.append(i)
print(sll.remove_by_value(6))

print('\n\n----')
sll.print_list()
print('\n')
