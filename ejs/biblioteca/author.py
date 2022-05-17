class Author:
    def __init__(self, name, nationality, birthday):
        self.name = name
        self.nationality = nationality
        self.birthday = birthday
    
    def __str__(self,):
        return f"{self.name}, {self.nationality}, {self.birthday}"