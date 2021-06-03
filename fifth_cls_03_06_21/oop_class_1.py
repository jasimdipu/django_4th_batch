class Student:
    # global variable, instance, attr
    stu_name = ""
    stu_dept = ""

    # constructor
    def __init__(self, name, dept):
        self.stu_name = name
        self.stu_dept = dept

    def get_student_name(self):
        return self.stu_name

    def set_student_name(self, name):
        self.stu_name = name

    def get_dep(self):
        return self.stu_dept

    # account = ""

    def set_dep(self, dept):
        self.stu_dept = dept


# create an object
student = Student("Jamil", "CSE")
print(student.stu_name, student.stu_dept)
student.set_student_name(input())
student.set_dep(input())
print(student.get_student_name(), student.get_dep())
