
class Student:
    def __init__(self, reg_no, student_name, access_number, course):
        self.reg_no = reg_no
        self.student_name = student_name
        self.access_number = access_number
        self.course = course

    def __str__(self):

        return(f"student details: {self.reg_no}, {self.student_name}, {self.access_number}, {self.course}")


Student_1=Student('S23B13/040','NADIYE ENOSI PETER', 'B24326', 'BSIT')

print(Student_1)