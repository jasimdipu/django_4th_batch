from emp_impl import EmployeeImpl


class EmpControler:

    def get_emp_info(self):
        e = EmployeeImpl()

        return e.get_emp_name()+e.get_dept()