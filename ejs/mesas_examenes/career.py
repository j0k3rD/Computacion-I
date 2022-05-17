from re import sub


class Career:
    def __init__(self, name, description, sub_list, students_list, university):
        self.name = name
        self.description = description
        self.sub_list = sub_list
        self.students_list = students_list
        self.university = university

    def __str__(self):
        return f"{self.name}, {self.description}, {self.description}, {self.sub_list}, {self.students_list}, {self.university}"

