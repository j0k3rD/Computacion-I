class Inscription:
    def __init__(self, student, subjet, ins_date):
        self.student = student
        self.subjet = subjet
        self.ins_date = ins_date

    def __str__(self):
        return f"{self.student},{self.subjet},{self.ins_date}"

