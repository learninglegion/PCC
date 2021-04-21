#11.1 test_cities
import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for city_country"""

    def test_city_country(self):
        """Do name like santiago chile work?"""
        formatted_name = city_country('evansville', 'indiana')
        self.assertEqual(formatted_name, 'Evansville, Indiana')

    def test_city_country(self):
        """Do name like santiago chile work?"""
        formatted_name = city_country('evansville', 'indiana', 150000)
        self.assertEqual(formatted_name, 'Evansville, Indiana - 150000')

if __name__ == '__main__':
    unittest.main()