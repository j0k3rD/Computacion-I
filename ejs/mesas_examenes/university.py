class University:
    def __init__(self, name, direction, web):
        self.name = name
        self.direction = direction
        self.web = web
    
    def __str__(self):
        return f"{self.name}, {self.direction}, {self.web}"




