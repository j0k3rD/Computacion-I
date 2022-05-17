from student import Student
from university import University
from subjet import Subjet
from inscription import Inscription
from career import Career

class Program:
    students = []
    subjects = []
    ing_subj = []
    psico_subj = []
    uni = []
    career_lst = []
    inscriptions = []


# Funcion para crear estudiante
    def add_student(self):
        name = input("Enter student name: ")
        surname = input("Enter student surname: ")
        id = int(input("Enter student id: "))
        mail = input("Enter student email: ")

        if len(str(id)) > 8:
            print("\nInvalid ID. Longer than 8 char. Try Again..")
            return None
        else:
            student = Student(name,surname,id,mail)
            self.students.append(student)
            print("Student Added!")
            return student


    #Funcion para crear universidad  
    def add_university(self):
        name = input("Enter university name: ")
        direction = input("Enter university direction: ")
        web = input("Enter university web: ")

        uni = University(name, direction, web)
        print("University Added!\n")
        self.uni.append(uni)
        return uni
    
    def verify_univ(self):
        uni_name = input("Enter the University name: ")
        for i in range(len(self.uni)):
            if self.uni[i].name == uni_name:
                return self.uni[i]
        return None

    #Funcion para crear Materia
    def add_sub(self):
        name = input("Enter subjet name: ")
        code = input("Enter subjet code: ")
        sub = Subjet(name,code)
        self.subjects.append(sub)

        if sub.code == range(0,30):
            self.ing_subj.append[sub]
        elif sub.code == range(30,60):
            self.psico_subj.append(sub)

        print("Subject Added!")
        return sub
    

    #Funcion para crear Carrera
    def add_career(self):
        name = input("Enter career name: ")
        des = input("Enter career description: ")
        subjs = self.add_subj_to_career()
        self.students
        self.uni
        
        career = Career(name, des, subjs, self.students, self.uni)
        self.career_lst.append(career)
        print("Career Added!")
        return career
    

    #Funcion crear Inscripcion
    def add_inscription(self):
        # if self.add_student() == None:
        #     return
        # else:
            if self.verify_univ() == None:
                print("Add a University first.")
                return
            else:
                if self.verif_subj() == None:
                    print("Add Subjects first.")
                    return
                else:
                    if self.verif_career() == None:
                        print("Add a Career first.")
                        return
                    else:
                        self.add_student()
                        student = self.verif_student()
                        sub = self.verif_subj()
                        self.add_subj_to_career()
                        self.verif_subj_inCareer()
                        date_ins = input("Enter the date of inscription: ")

                        ins = Inscription(student, sub, date_ins)

                        self.inscriptions.append(ins)
                        print("Inscription Made!\n")
                        print(self.show_inscription())

                        return ins    


    def verif_student(self):
        print("\nVerifying student in system..\n")
        name = input("Enter the student name: ")
        for i in range(len(self.students)):
            if self.students[i].name == name:
                print(f"{name} was found!")
                return self.students[i]
            else:
                print("Student Not Found")
        return None


    def verif_subj(self):
        name = input("Enter the subject name: ")
        for i in range(len(self.subjects)):
            if self.subjects[i].name == name:
                return self.subjects[i]
            else:
                print("Subject Not Found")
        return None

    def verif_career(self):
        name = input("Enter the career name: ")
        for i in range(len(self.career_lst)):
            if self.career_lst[i].name == name:
                return self.career_lst[i]
            else:
                print("Career Not Found")
        return None

    def add_subj_to_career(self):
        for i in range(len(self.career_lst)):
            if self.career_lst[i].name == "Ingenieria Informatica":
                subjs = self.ing_subj
            elif self.career_lst[i].name == "Psicologia":
                subjs = self.psico_subj


    def verif_subj_inCareer(self):
        name = input("Enter the subject name: ")
        for i in range(len(self.subjects)):
            if self.subjects[i].name == name:
                return self.subjects[i]
            else:
                print("Subject Not Found")
        return None


    def show_inscription(self):
        for i in range(len(self.inscriptions)):
            return self.inscriptions[i]
