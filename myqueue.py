class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None 

    def __str__(self): 
        return f'<Node: {self.value}>'

class Queue: 
    def __init__(self, value): 
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node 
        self.length = 1 

    def show_queue(self): 
        temp = self.first 
        while temp: 
            print(temp)
            temp = temp.next 

    def enqueue(self, value): 
        new_node = Node(value)
        if self.length == 0: 
            self.first = new_node 
            self.last = new_node 
        else: 
            self.last.next = new_node 
            self.last = new_node  
        self.length += 1 
        return True 
    
    def dequeue(self): 
        if self.length == 0: 
            return None
        temp = self.first  
        if self.length == 1: 
            self.first = None 
            self.last = None 
        else: 
            self.first = self.first.next 
            temp.next = None 
        self.length -= 1 
        return temp 


        
q = Queue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

q.show_queue()