from emp_impl import EmployeeImpl


class EmployeeInfo(EmployeeImpl):

    def __init__(self, name, dept, address):
        super(EmployeeInfo, self).__init__(emp_name=name, emp_dept=dept)
        self.__address = address

    def getAddress(self): return self.__address


emp_inf = EmployeeInfo("Safin", "Marketing", "Dhaka")
print(emp_inf.get_emp_name())
print(emp_inf.get_dept())
print(emp_inf.getAddress())
