class Employee:
    """
    Class for an employee with first/last name
    and annual salary
    """
    def __init__(self, firstn, lastn, salary):
        """get employee info"""
        self.firstn = firstn
        self.lastn = lastn
        self.salary = salary

    def give_raise(self, payincrease=5000):
        self.salary = self.salary + payincrease
#        if payincrease:
#            self.salary = self.salary + payincrease
#        else:
#            self.salary = self.salary + 5000

#my_employee = Employee('brent', 'beckwith', 50000)
#print(my_employee.salary)
#my_employee.give_raise(2222)
#print(my_employee.salary)