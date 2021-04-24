##11.1 and 11.2 test_cities
#import unittest
#from city_functions import city_country
#
#class CityCountryTestCase(unittest.TestCase):
#    """Test for city_country"""
#
#    def test_city_country(self):
#        """Do name like santiago chile work?"""
#        formatted_name = city_country('evansville', 'indiana')
#        self.assertEqual(formatted_name, 'Evansville, Indiana')
#
#    def test_city_country(self):
#        """Do name like santiago chile work?"""
#        formatted_name = city_country('evansville', 'indiana', 150000)
#        self.assertEqual(formatted_name, 'Evansville, Indiana - 150000')
#
#if __name__ == '__main__':
#    unittest.main()

#11.3
import unittest
from employee_chap11 import Employee

class TestEmployee(unittest.TestCase):
    """test setup for employee tests"""

    def setUp(self):
        self.firstn = 'Brent'
        self.lastn = 'Beckwith'
        self.salary = 50000
        self.my_employee = Employee(self.firstn, self.lastn, self.salary)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.salary + 5000, 55000)

    def test_give_custom_raise(self):
        self.payincrease = 25000
        self.newsalary = self.salary + self.payincrease
        self.my_employee.give_raise(self.payincrease)
        self.assertEqual(self.salary + self.payincrease, self.newsalary)

if __name__ == '__main__':
    unittest.main()