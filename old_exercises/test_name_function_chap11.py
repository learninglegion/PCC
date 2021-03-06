#test_name_function
import unittest
from name_function_chap11 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like janis joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_middle_last_name(self):
        """Do names like janis anne joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin', 'anne')
        self.assertEqual(formatted_name, 'Janis Anne Joplin')

if __name__ == '__main__':
    unittest.main()
