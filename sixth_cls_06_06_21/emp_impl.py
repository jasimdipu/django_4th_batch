from oop_principle import Employee


class EmployeeImpl(Employee):
    # __emp_name = ""
    # __emp_dept = ""

    def __init__(self, emp_name, emp_dept):
        self.__emp_name = emp_name
        self.__emp_dept = emp_dept

    def get_emp_name(self):
        return self.__emp_name

    def set_emp_name(self, name):
        self.__emp_name = name

    def get_dept(self):
        return self.__emp_dept

    def set_dept(self, dept):
        self.__emp_dept = dept




