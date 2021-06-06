# abstraction, encapsulation, inheritance, polymorphism

from abc import ABC


class Employee(ABC):

    def get_emp_name(self):
        pass

    def set_emp_name(self, name):
        pass

    def get_dept(self):
        pass

    def set_dept(self, dept):
        pass
