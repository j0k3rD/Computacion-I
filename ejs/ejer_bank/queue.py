class Queue:
    def __init__(self):
        self.list = []
    
    def push(self, element):
        self.list.append(element)
    
    def pop(self):
        if len(self.list) > 0:
            return self.list.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.list)