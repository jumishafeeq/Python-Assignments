# Module employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return f"Name : {self.name}"

    def get_salary(self):
        return f"Salary : {self.salary}"