class Student:
    def __init__(self, name, surname, id, email):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.id}, {self.email}"

    