class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, element):
        self.list.append(element)
    
    def size(self):
        return len(self.list)
    
    def peek(self):
        if len(self.list) > 0:
            return self.list[len(self.list) - 1]
        else:
            return None
    
    def empty(self):
        if len(self.list) > 0:
            return False
        else:
            return True
